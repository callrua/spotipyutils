# Used to pull and parse setlist from setlist.fm

# import libs
import urllib2
import os
import argparse
import spotipy
import spotipy.util as util
from bs4 import BeautifulSoup


def pull_artist(site):
    # query the website and return the html to the variable page
    page = urllib2.urlopen(site)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    artist_name_box = soup.find('div', attrs={'class': 'setlistHeadline'})
    artist_name = artist_name_box.text.strip()
    return artist_name.split('Edit venue', 1)[0].rstrip().replace('\n', ' ')


def pull_setlist(site):
    # query the website and return the html to the variable page
    page = urllib2.urlopen(site)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    songs_html = soup.find_all('a', attrs={'class': 'songLabel'})
    songs = []
    for song in songs_html:
        songs.append(song.text.strip())
    return songs


def create_playlist(playlist_name):
    sp.user_playlist_create(username, playlist_name)


def add_to_playlist(playlist_songs, playlist_artist):
    playlists = sp.user_playlists(username, limit=1)
    for playlist in playlists['items']:
        for s in playlist_songs:
            search_string = s + ' artist:' + playlist_artist.split('Setlist at ', 1)[0]
            search_song = sp.search(q=search_string, type='track', limit=1)
            for song in search_song['tracks']['items']:
                song_uri = song['uri']
                tracks = [song_uri]
                sp.user_playlist_add_tracks(username, playlist_id=playlist['id'], tracks=tracks,
                                            position=None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Args')
    parser.add_argument('--user-id', '-u', dest='uid', type=str, required=True,
                        help='Your Spotify user ID')
    parser.add_argument('--setlist', '-s', dest='setlist', type=str, required=True,
                        help='Your setlist.fm link')
    args = parser.parse_args()
    #song_page = 'https://www.setlist.fm/setlist/the-wonder-years/2018/stylus-leeds-england-3ece5af.html'
    song_page = args.setlist
    username = args.uid
    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
    scope = "playlist-modify-private, playlist-modify-public"

    token = util.prompt_for_user_token(username, scope,
                                       client_id,
                                       client_secret,
                                       'http://localhost/')
    if token:
        sp = spotipy.Spotify(auth=token)
        artist = pull_artist(song_page)
        create_playlist(artist)

        songs = pull_setlist(song_page)
        add_to_playlist(songs, artist)
    else:
        print "Can't get token for", username






