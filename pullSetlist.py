# Used to pull and parse setlist from setlist.fm
# example setlist; https://www.setlist.fm/setlist/marmozets/2018/kilby-court-salt-lake-city-ut-6bef8652.html

# import libs
import urllib2
from bs4 import BeautifulSoup

# url declare
song_page = 'https://www.setlist.fm/setlist/marmozets/2018/kilby-court-salt-lake-city-ut-6bef8652.html'

# query the website and return the html to the variable page
page = urllib2.urlopen(song_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

print('Artist:')
artist_name_box = soup.find('div', attrs={'class': 'setlistHeadline'})
artist_name = artist_name_box.text.strip()
print artist_name.split(' ', 1)[0]

print("\n"'Setlist:')
songs_html = soup.find_all('a', attrs={'class': 'songLabel'})
for song in songs_html:
    print song.text.strip()





