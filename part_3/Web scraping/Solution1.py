import requests
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture"
resp = requests.get(url)
soup = bs(resp.text, 'html.parser')
type(soup)

winners = []

winners_rows = soup.find_all('tr', style="background:#FAEB86")
for item in winners_rows:
    winners.append(str(item.a.string))
print(winners)