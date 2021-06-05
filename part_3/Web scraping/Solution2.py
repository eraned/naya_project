import requests
from bs4 import BeautifulSoup as bs

episodes_rating_list = []
seasons=8

for season in range(1, seasons+1):
    url = f'https://www.imdb.com/title/tt0944947/episodes?season={season}'
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    episodes = soup.find_all('div', class_="list_item")
    for episode in episodes:
        episode_num = int(episode.find('meta', itemprop='episodeNumber')['content'])
        episode_rating = float(episode.find('span', class_='ipl-rating-star__rating').string)
        episodes_rating_list.append((season, episode_num, episode_rating))
print(episodes_rating_list)