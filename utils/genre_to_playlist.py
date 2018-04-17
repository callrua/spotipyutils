"""This script generates a spotify playlist of up to 100 songs based on given genres"""
import argparse
import spotipy
import spotipy.util as util
import os
import datetime
from pprint import pprint
import sys

parser = argparse.ArgumentParser(description='Args')
parser.add_argument('--genres', '-g', dest='genres', required=True, nargs='+',
                    help='Specify the genre(s) of music you wish to create a playlist for. '
                         'The list should be space seperated e.g. trance hip-hop trip-hop')
parser.add_argument('--track-limit', '-l', dest='limit', type=int, default=100, required=False,
                    help='The maximum number of tracks you want on the playlist')
parser.add_argument('--user-id', '-u', dest='uid', required=True,
                    help='Your spotify userID')
args = parser.parse_args()


class Spotify:
    def __init__(self):
        self.uid = args.uid
        self.genres = args.genres
        self.limit = args.limit
        self.modify_scope = 'playlist-modify-public'
        self.token = util.prompt_for_user_token(username=self.uid, scope=self.modify_scope)
        self.spotify = spotipy.Spotify(auth=self.token)
        self.curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.playlist_name = ("%s %s" % (str(self.genres), str(self.curr_time)))

    def main(self):
        create_blank_playlist(self)
        accepted_genre_list = self.spotify.recommendation_genre_seeds()['genres']
        for i in self.genres:
            if i not in accepted_genre_list:
                print("ERROR\n%s is not a recognised genres. "
                      "Please choose any from the following list of accepted genres:\n" % i)
                pprint("%s" % accepted_genre_list)
                sys.exit(1)
        populate_playlist(self)


def create_blank_playlist(self):
    self.spotify.user_playlist_create(user=self.uid, name=self.playlist_name)


def populate_playlist(self):
    tracks = []
    playlists = self.spotify.user_playlists(user=self.uid)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            if self.playlist_name in playlist['name']:
                while len(tracks) < self.limit:
                    reccs = self.spotify.recommendations(seed_genres=self.genres, limit=1)
                    for j, track in enumerate(reccs['tracks']):
                        tracks.append(track['id'])
                self.spotify.user_playlist_add_tracks(user=self.uid, playlist_id=playlist['id'], tracks=tracks)
                print("Succesfully added at least %s songs to your new playlist %s\nENJOY :)"
                      % (self.limit, self.playlist_name))
        if playlists['next']:
            playlists = self.spotify.next(playlists)
        else:
            playlists = None


if __name__ == '__main__':
    Spotify().main()
