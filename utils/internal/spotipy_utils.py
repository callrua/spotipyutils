import os
import sys
import datetime

import click
import spotipy
import spotipy.util as util
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Spotify:
    def __init__(self):
        self.id = id
        self.scope = "playlist-modify-private, playlist-modify-public"
        self.token = util.prompt_for_user_token(self.id, self.scope)
        self.spotify = spotipy.Spotify(auth=self.token)

    def setlist_to_playlist(self, setlist_url):
        """ Create a Spotify Playlist from a Setlist.fm URL."""
        # Parse the Artist's name from the HTML
        page = urlopen(setlist_url)
        soup = BeautifulSoup(page, 'html.parser')
        artist_name_box = soup.find('div', attrs={'class': 'setlistHeadline'})
        artist_name = artist_name_box.text.strip()
        artist = artist_name.split('Edit venue', 1)[0].rstrip().replace('\n', ' ').replace('Setlist at', '@')

        # Create a blank Spotify playlist
        self.spotify.user_playlist_create(self.id, artist)

        # Parse the setlist's songs from the HTML
        page = urlopen(setlist_url)
        soup = BeautifulSoup(page, 'html.parser')
        songs_html = soup.find_all('a', attrs={'class': 'songLabel'})
        songs = [s.text.strip() for s in songs_html]

        # Add the setlist's songs to the Spotify playlist
        playlists = self.spotify.user_playlists(self.id, limit=1)
        for playlist in playlists['items']:
            for s in songs:
                search_string = s + ' artist:' + artist.split('@ ', 1)[0]
                search_song = self.spotify.search(q=search_string, type='track', limit=1)
                for song in search_song['tracks']['items']:
                    song_uri = song['uri']
                    tracks = [song_uri]
                    self.spotify.user_playlist_add_tracks(self.id, playlist_id=playlist['id'], tracks=tracks,
                                                position=None)


    def add_top_to_playlist(self, song_name, song_artist):
        playlists = self.spotify.user_playlists(self.id, limit=1)
        for playlist in playlists['items']:
            search_string = song_name + ' artist:' + song_artist
            search_song = self.spotify.search(q=search_string, type='track', limit=1)
            for song in search_song['tracks']['items']:
                song_uri = song['uri']
                tracks = [song_uri]
                self.spotify.user_playlist_add_tracks(self.id, playlist_id=playlist['id'], tracks=tracks,
                                            position=None)


    def top_tracks_to_playlist(self):
        ranges = ['short_term', 'medium_term', 'long_term']
        time_now = datetime.datetime.now()
        datestamp = time_now.strftime("%Y%m%d")
        for r in ranges:
            playlist_name = "{0} {1} top tracks".format(datestamp, r)
            self.spotify.user_playlist_create(self.id, playlist_name)
            results = self.spotify.current_user_top_tracks(time_range=r, limit=100)
            for i, item in enumerate(results['items']):
                song = item['name']
                artist = item['artists'][0]['name']
                self.add_top_to_playlist(song, artist)


