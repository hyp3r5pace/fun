import requests
from bs4 import BeautifulSoup
import random


wiki_page = {'Search_engine': 'Search Engine'}

BASE_URL='https://en.wikipedia.org/wiki/'
URL = BASE_URL + 'Mainsail'
count = 0

while True:
    print('Scraping ' + URL)
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    all_paragraph = soup.find_all('p')

    for para in all_paragraph:
        if para.find('a', recursive=False):
            href = para.find('a', recursive=False).get('href').split('/')[2]
            title = para.find('a', recursive=False).get('title')
            break

    if wiki_page.get(href) is None:
        count += 1
        wiki_page[href] = title
        URL = BASE_URL + href
        print('No of pages visited: ', count)
        print('Next --> ' + title)
    else:
        print('\nCycle detected\n')
        print('Already visited topic wikipedia page ' + BASE_URL + href)
        break



