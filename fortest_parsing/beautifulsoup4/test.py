from bs4 import BeautifulSoup
import requests


base = 'https://ru.stackoverflow.com'


html = requests.get(base).content


soup = BeautifulSoup(html, 'lxml')

div = soup.find('div', id='question-mini-list')


print(div)