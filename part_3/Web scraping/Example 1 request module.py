'''
The site SongLyrics contains the lyrics of songs.
In this exercise we scrape the words of a desired song.
with request package

Much of the main functionalities of the module are implemented through the class response, whose properties give
access to the HTTP response.
'''

import requests

artist = 'the-beatles'
song = 'two-of-us'
url = f'http://www.songlyrics.com/{artist}/{song}-lyrics/'

resp = requests.get(url)

# print the status code
print(resp.status_code)

# Print the url that we requested
print(resp.url)

# Print the text that response
print(resp.text[:1500])