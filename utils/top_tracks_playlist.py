# Creates a Spotify playlist of users top tracks

# import libs
import argparse
import spotipy
import spotipy.util as util
import datetime


def create_playlist(playlist_name):
    sp.user_playlist_create(username, playlist_name)


def add_to_playlist(song_name, song_artist):
    playlists = sp.user_playlists(username, limit=1)
    for playlist in playlists['items']:
        search_string = song_name + ' artist:' + song_artist
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

    args = parser.parse_args()
    username = args.uid
    scope = "playlist-modify-private, playlist-modify-public, user-top-read"
    token = util.prompt_for_user_token(username, scope)
    datetime = datetime.datetime.now()
    datestamp = datetime.strftime("%Y%m%d")

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        ranges = ['short_term', 'medium_term', 'long_term']
        for r in ranges:
            playlist_name = "{0} {1} top tracks".format(datestamp, r)
            create_playlist(playlist_name)
            results = sp.current_user_top_tracks(time_range=r, limit=100)
            for i, item in enumerate(results['items']):
                song = item['name']
                artist = item['artists'][0]['name']
                add_to_playlist(song, artist)
    else:
        print("Can't get token for {0}".format(username))
