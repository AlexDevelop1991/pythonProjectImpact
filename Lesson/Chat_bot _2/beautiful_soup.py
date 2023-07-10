import requests
from bs4 import BeautifulSoup


def scrape_data():
    # Make a GET request to the Google News homepage
    response = requests.get('https://999.md/ru/list/phone-and-communication/mobile-phones')
    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all the news articles on the page
    news_articles = soup.find_all('li', class_='ads-list-photo-item')
    # Iterate through the articles and extract the title, and link
    phones = []
    for article in news_articles:
        try:
            if article:
                title = article.find('div', class_='ads-list-photo-item-title').text
                image = article.find('img')['src']
                link = article.find('a')['href']
                # Print the extracted information
                print(title)
                print(image)
                print('https://999.md/' + link)
                phones.append('https://999.md/' + link)
        except:
            pass
    return phones


scrape_data()

def computer():
    response = requests.get('https://999.md/ru/list/computers-and-office-equipment/laptops')

    soup = BeautifulSoup(response.text, 'html.parser')

    news_articles = soup.find_all('li', class_='ads-list-photo-item')

    computers = []
    for article in news_articles:
        try:
            if article:
                title = article.find('div', class_='ads-list-photo-item-title').text
                image = article.find('img')['src']
                link = article.find('a')['href']
                # Print the extracted information
                print(title)
                print(image)
                print('https://999.md/' + link)
                computers.append('https://999.md/' + link)
        except:
            pass
    return computers


