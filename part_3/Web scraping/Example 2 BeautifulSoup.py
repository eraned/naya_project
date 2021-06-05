'''
The Eucalyptus is a high-end restaurant in Jerusalem, and their menu can be found here.
Scrape their site in order to make a simplified list of the dishes and their prices.
'''
import requests
from bs4 import BeautifulSoup as bs
import re

url = "http://www.the-eucalyptus.com/menu/"
resp = requests.get(url)
soup = bs(resp.text, 'html.parser')

# By exploring the site source code we see that the dishes are marked by the 'article' tags and the class 'menu-item'.
dishes_tags = soup.find_all(name='article', class_='menu-item')
print(dishes_tags[0].prettify())

# extracting the dish and price out of each 'article' tag.
dishes = [str(x.find(name='p').string.strip())
          for x in dishes_tags]

prices = [str(x.find(name='span').string.strip())
          for x in dishes_tags]

# Zipping them together.
for dish, price in zip(dishes, prices):
    print('{:35} {}'.format(dish, price))