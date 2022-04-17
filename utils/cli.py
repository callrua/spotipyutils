import os
import sys
import datetime

import click
import spotipy
import spotipy.util as util
from urllib.request import urlopen
from bs4 import BeautifulSoup


CONTEXT_SETTINGS = dict(auto_envvar_prefix="SPOTIFY")


class Spotify:
    def __init__(self):
        self.id = id
        self.scope = "playlist-modify-private, playlist-modify-public"
        self.token = util.prompt_for_user_token(self.id, self.scope)
        self.spotify = spotipy.Spotify(auth=self.token)

    def greet(self, message):
        print(f"Hi this is the {message}")

    def setlist_to_playlist(self, setlist_url):
        """ Create a Spotify Playlist from a Setlist.fm URL."""
        print(f"Username is: {self.id}")
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


pass_environment = click.make_pass_decorator(Spotify, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))


class SpotifyCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename in os.listdir(cmd_folder):
                if filename.endswith(".py") and filename.startswith("cmd_"):
                    rv.append(filename[4:-3])
        rv.sort()
        return rv


    def get_command(self, ctx, name):
        try:
            mod = __import__(f"utils.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=SpotifyCLI, context_settings=CONTEXT_SETTINGS)
@click.option("--id", type=str, help="ID of User who will own the playlist")
@pass_environment
def cli(ctx, id):
    ctx.id = id
