import json
import requests
import time
import urllib
import logging
import signal
import sys


TOKEN = '5616580938:AAFUHuYdqqbV2CmKXMoSQjYMzeJuLKSU81E'
OWN_KEY = '40980343d739a08f12561866f7373508'
POLLING_TIMEOUT = None


# Lambda functions to parse updates from Telegram
def get_text(update): return update['message']['text']
def get_location(update): return update['message']['location']
def get_chat_id(update): return update['message']['chat']['id']
def get_up_id(update): return int(update['update_id'])
def get_result(update): return update['result']


# Lambda functions to parse weather responses
def get_desc(w): return w['weather'][0]['description']
def get_temp(w): return w['main']['temp']
def get_city(w): return w['name']


logger = logging.getLogger('weather-telegram')
logger.setLevel(logging.DEBUG)


# Cities for weather requests
cities = ['London', 'Chisinau']


def sig_handler(signal, frame):
    logger.info('SIGINT received. Exiting... Bye Bye')
    sys.exit(0)


# Configure file and console logging
def config_logging():
    # Create file logger and set level to DEBUG
    # Mode = write -> clear existing log file
    handler = logging.FileHandler('run.log', mode='w')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Create console handler and set level to INFO
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('[%levelname)s] - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def parse_config():
    global URL, URL_OWM, POLLING_TIMEOUT
    URL = f'https://api.telegram.org/bot{TOKEN}/'
    URL_OWM = f'https://api.openweathermap.org/data/2.5/weather?appid={OWN_KEY}&units=metric'


# Make a request to Telegram bot and get JSON response
def make_request(url):
    logger.debug('URL: %s' % url)
    r = requests.get(url)
    resp = json.loads(r.content.decode('utf8'))
    return resp


# Return all the updates with ID > offset
# (Updates list is kept by Telegram for 24h)
def get_updates(offset=None):
    url = URL + 'getUpdates?timeout=%s' % POLLING_TIMEOUT
    logger.info('Getting updates')
    if offset:
        url += f'&offset={offset}'
    js = make_request(url)
    return js


# Build a one-time keyboard for on-screen options
def build_keyboard(items):
    keyboard = [[{'text': item}] for item in items]
    reply_keyboard = {'keyboard': keyboard, 'one_time_keyboard': True}
    logger.debug(reply_keyboard)
    return json.dumps(reply_keyboard)


def build_cities_keyboard():
    keyboard = [[{'text': c}] for c in cities]
    keyboard.append([{'text': 'Share location', 'request_location': True}])
    reply_keyboard = {'keyboard': keyboard, 'one_time_keyboard': True}
    logger.debug(reply_keyboard)
    return json.dumps(reply_keyboard)


# Query OWM for the weather for place or coords
def get_weather(place):
    if isinstance(place, dict):  # coordinates provided
        lat, lon = place['latitude'], place['longitude']
        url = URL_OWM + '&lat=%f&lon=%f&cnt=1' % (lat, lon)
        logger.info('Requesting weather: ' + url)
        js = make_request(url)
        logger.debug(js)
        return u'%s \N{DEGREE SIGN}C, %s in %s' % (get_temp(js), get_desc(js), get_city(js))
    else:
        # Make req
        url = URL_OWM + f'&q={place}'
        logger.info('Requesting weather: ' + url)
        js = make_request(url)
        logger.debug(js)
        return u'%s \N{DEGREE SIGN}C, %s in %s' % (get_temp(js), get_desc(js), get_city(js))


# Send URL-encoded message to chat id
def send_message(text, chat_id, interface=None):
    text = text.encode('utf-8', 'strict')
    text = urllib.parse.quote_plus(text)
    url = URL + f'sendMessage?text={text}&chat_id={chat_id}&parse_mode=Markdown'
    if interface:
        url += f'&reply_markup={interface}'
    requests.get(url)


# Get the ID of the last available update
def get_last_update_id(updates):
    ids = []
    for update in get_result(updates):
        ids.append(get_up_id(update))
    return max(ids)


# Keep track of conversation states: 'weatherReq'
chats = {}


# Echo all message back
def handle_updates(updates):
    for update in get_result(updates):
        chat_id = get_chat_id(update)
        try:
            text = get_text(update)
        except Exception as e:
            logger.error('No text field in update. Try to get location')
            loc = get_location(update)
            # Was weather previously requested?
            if (chat_id in chats) and (chats[chat_id] == 'weatherReq'):
                logger.info('Weather requested for %s in chat id %d' % (str(loc), chat_id))
                # Send weather to chat id and clear state
                send_message(get_weather(loc), chat_id)
                del chats[chat_id]
            continue

        if text == '/weather':
            keyboard = build_cities_keyboard()
            chats[chat_id] = 'weatherReq'
            send_message('Select a city', chat_id, keyboard)
        elif text == '/start':
            send_message("Cahn's Axiom: When all else fails, read the instructions", chat_id)
        elif text.startswith('/'):
            logger.warning('Invalid command %s' % text)
            continue
        elif (text in cities) and (chat_id in chats) and (chats[chat_id] == 'weatherReq'):
            logger.info('Weather requested for %s' % text)
            # Send weather to chat id and clear state
            send_message(get_weather(text), chat_id)
            del chats[chat_id]
        else:
            keyboard = build_keyboard(['/weather'])
            send_message(
                'I learn new things every day but for now you can ask me about the weather.', chat_id, keyboard
            )


def main():
    # Set up file and console loggers
    config_logging()
    # Get tokens and keys
    parse_config()
    # Intercept Ctrl-C SIGINT
    signal.signal(signal.SIGINT, sig_handler)
    # Main loop
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(get_result(updates)) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
            time.sleep(0.5)


if __name__ == '__main__':
    main()
