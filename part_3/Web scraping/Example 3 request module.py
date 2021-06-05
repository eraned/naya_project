'''
The site SongLyrics contains the lyrics of songs.
In this exercise we scrape the words of a desired song.
with request package

Much of the main functionalities of the module are implemented through the class response, whose properties give
access to the HTTP response.
'''

import requests

artist = 'the-beatles'
song = 'let-it-be'
url = f'http://www.songlyrics.com/{artist}/{song}-lyrics/'
print(url, '\n')
resp = requests.get(url)
text = resp.content.decode('utf-8').split('\n')
song = []
song_line = False
lyrics_part_identifier = '<p id="songLyricsDiv"  class="songLyricsV14 iComment-text">'
for line in text:
    if lyrics_part_identifier in line:
        line = line.replace(lyrics_part_identifier, '')
        song_line = True
    if song_line:
        if line.strip() == '</div>':
            break
        song.append(line.strip().replace('<br />', '').replace('</p>', ''))
lyrics = '\n'.join(song)
print(lyrics)
