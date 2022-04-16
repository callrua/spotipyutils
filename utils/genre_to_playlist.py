"""This script generates a spotify playlist of up to 100 songs based on given genres"""
import spotipy
import spotipy.util as util
import datetime
from pprint import pprint
import sys


class GenreToPlaylist:
    def __init__(self, uid):
        self.playlist_name = None
        self.genres = None
        self.limit = None
        self.uid = uid
        self.modify_scope = 'playlist-modify-public'
        self.token = util.prompt_for_user_token(username=self.uid, scope=self.modify_scope)
        self.spotify = spotipy.Spotify(auth=self.token)
        self.curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_playlist(self, genres, limit):
        self.genres = genres
        self.limit = limit
        self.check_genres(self.get_genres())
        self.set_playlist_name()
        self.create_blank_playlist()
        self.populate_playlist()

    def check_genres(self, accepted_genre_list):
        for i in self.genres:
            if i not in accepted_genre_list:
                print("ERROR\n%s is not a recognised genre. "
                      "Please choose any from the following list of accepted genres:\n" % i)
                pprint("%s" % accepted_genre_list)
                sys.exit(1)

    def get_genres(self):
        return self.spotify.recommendation_genre_seeds()['genres']

    def create_blank_playlist(self):
        self.spotify.user_playlist_create(user=self.uid, name=self.playlist_name)

    def set_playlist_name(self):
        playlist_name = ''
        for i in self.genres:
            playlist_name += i + "/"
        self.playlist_name = "%s %s" % (playlist_name[:-1], str(self.curr_time))

    def populate_playlist(self):
        tracks = []
        playlists = self.spotify.user_playlists(user=self.uid)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                if self.playlist_name in playlist['name']:
                    while len(tracks) < int(self.limit):
                        reccs = self.spotify.recommendations(seed_genres=self.genres, limit=1, country='GB')
                        for j, track in enumerate(reccs['tracks']):
                            tracks.append(track['id'])
                    self.spotify.user_playlist_add_tracks(user=self.uid, playlist_id=playlist['id'], tracks=tracks)
                    print("Succesfully added %s songs to your new playlist %s\nENJOY :)"
                          % (self.limit, self.playlist_name))
            if playlists['next']:
                playlists = self.spotify.next(playlists)
            else:
                playlists = None
