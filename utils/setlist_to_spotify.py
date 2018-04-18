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
    return artist_name.split('Edit venue', 1)[0].rstrip().replace('\n', ' ').replace('Setlist at', '@')


def pull_setlist(site):
    # query the website and return the html to the variable page
    page = urllib2.urlopen(site)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    songs_html = soup.find_all('a', attrs={'class': 'songLabel'})
    return [songs.text.strip() for songs in songs_html]


def create_playlist(playlist_name):
    sp.user_playlist_create(username, playlist_name)


def add_to_playlist(playlist_songs, playlist_artist):
    playlists = sp.user_playlists(username, limit=1)
    for playlist in playlists['items']:
        for s in playlist_songs:
            search_string = s + ' artist:' + playlist_artist.split('@ ', 1)[0]
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
    song_page = args.setlist
    username = args.uid
    scope = "playlist-modify-private, playlist-modify-public"
    token = util.prompt_for_user_token(username, scope)
    if token:
        sp = spotipy.Spotify(auth=token)
        artist = pull_artist(song_page)
        create_playlist(artist)

        songs = pull_setlist(song_page)
        add_to_playlist(songs, artist)
    else:
        print "Can't get token for", username
