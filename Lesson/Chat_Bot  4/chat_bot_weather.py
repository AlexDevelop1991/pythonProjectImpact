import json
import requests
import time
import urllib
import logging
import signal
import sys


TOKEN = ''
OWN_KEY = ''
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
