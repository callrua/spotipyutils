# Used to pull and parse setlist from setlist.fm
# example setlist; https://www.setlist.fm/setlist/marmozets/2018/kilby-court-salt-lake-city-ut-6bef8652.html

# import libs
import re
import urllib2
from bs4 import BeautifulSoup

# url declare
# quote_page = 'https://www.bloomberg.com/quote/SPX:IND

song_page = 'https://www.setlist.fm/setlist/marmozets/2018/kilby-court-salt-lake-city-ut-6bef8652.html'

# query the website and return the html to the variable page
page = urllib2.urlopen(song_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

print('Artist:')
# artist_name_box = soup.find('a', attrs={'title': 'More Marmozets setlists'})
artist_name_box = soup.find('div', attrs={'class': 'setlistHeadline'})

artist_name = artist_name_box.text.strip()
print artist_name.split(' ', 1)[0]

# Take out the <div> of name and get its value
print("\n"'Setlist:')
first_song_html = soup.find('a', attrs={'class': 'songLabel'})
next_song_html = first_song_html.find_next_sibling('a', attrs={'class': 'songLabel'})

print first_song_html
print next_song_html
first_song = first_song_html.text.strip()

setlist_html = soup.find('div', attrs={'class': 'setlistList'})
print setlist_html


print first_song


