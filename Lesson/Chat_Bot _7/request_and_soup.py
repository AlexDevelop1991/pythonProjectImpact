import requests
from bs4 import BeautifulSoup

# Beautiful Soup — это библиотека Python для извлечения данных из файлов HTML и XML

def request_sneakers_man():
    response_man = requests.get('https://999.md/ru/list/clothes-and-shoes/sports-shoes?hide_duplicates=no&buy_online=no&applied=1&ef=2104,2107,2111&o_2111_755=18603')
    soup = BeautifulSoup(response_man.text)
    news_articles = soup.find_all()
    sneakers = []
    for article in news_articles:
        try:
            if article:
                title = article.find('div', class_='ads-list-photo-item-title').text
                image = article.find('img')['src']
                link = article.find('a')['href']
                print(title)
                print(image)
                print('https://999.md/' + link)
                sneakers.append('https://999.md/' + link)

        except:
            pass
    return sneakers


def request_sneakers_woman():
    response_woman = requests.get('https://999.md/ru/list/clothes-and-shoes/sports-shoes?hide_duplicates=no&buy_online=no&applied=1&ef=2104,2107,2111&o_2111_755=18604')
    soup = BeautifulSoup(response_woman.text)
    news_articles = soup.find_all()
    sneakers = []
    for article in news_articles:
        try:
            if article:
                title = article.find('div', class_='ads-list-photo-item-title').text
                image = article.find('img')['src']
                link = article.find('a')['href']
                print(title)
                print(image)
                print('https://999.md/' + link)
                sneakers.append('https://999.md/' + link)

        except:
            pass
    return sneakers


def request_sneakers_boy():
    response_boy = requests.get('https://999.md/ru/list/clothes-and-shoes/childrens-shoes?hide_duplicates=no&buy_online=no&applied=1&show_all_checked_childrens=no&ef=2054,2057,2058&o_2057_620=18731&o_2058_755=18724')
    soup = BeautifulSoup(response_boy.text)
    news_articles = soup.find_all()
    sneakers = []
    for article in news_articles:
        try:
            if article:
                title = article.find('div', class_='ads-list-photo-item-title').text
                image = article.find('img')['src']
                link = article.find('a')['href']
                print(title)
                print(image)
                print('https://999.md/' + link)
                sneakers.append('https://999.md/' + link)

        except:
            pass
    return sneakers


def request_sneakers_girl():
    response_girl = requests.get('https://999.md/ru/list/clothes-and-shoes/childrens-shoes?hide_duplicates=no&buy_online=no&applied=1&show_all_checked_childrens=no&ef=2054,2057,2058&o_2057_620=18731&o_2058_755=18725')
    soup = BeautifulSoup(response_girl.text)
    news_articles = soup.find_all()
    sneakers = []
    for article in news_articles:
        try:
            if article:
                title = article.find('div', class_='ads-list-photo-item-title').text
                image = article.find('img')['src']
                link = article.find('a')['href']
                print(title)
                print(image)
                print('https://999.md/' + link)
                sneakers.append('https://999.md/' + link)

        except:
            pass
    return sneakers




