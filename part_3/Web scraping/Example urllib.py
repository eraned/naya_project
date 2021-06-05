'''
The site SongLyrics contains the lyrics of songs.
In this exercise we scrape the words of a desired song.
'''

import urllib.request

artist = 'the-beatles'
song = 'let-it-be'

url = f'http://www.songlyrics.com/{artist}/{song}-lyrics/'
print(url)

# if headers are needed:
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
text = resp.read().decode('utf-8')


print(text[:1000])
