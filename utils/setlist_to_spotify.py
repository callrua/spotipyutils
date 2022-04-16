# Used to pull and parse setlist from setlist.fm

# import libs
import argparse
import spotipy
import spotipy.util as util
import click

from commands.setlist_to_playlist import create_playlist_from_setlist


class Spotify:
    def __init__(self, uid):
        self.uid = uid
        self.scope = "playlist-modify-private, playlist-modify-public"
        self.token = util.prompt_for_user_token(self.uid, self.scope)
        self.spotify = spotipy.Spotify(auth=self.token)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Args')
    parser.add_argument('--user-id', '-u', dest='uid', type=str, required=True,
                        help='Your Spotify user ID')
    parser.add_argument('--setlist', '-s', dest='setlist', type=str, required=True,
                        help='Your setlist.fm link')
    args = parser.parse_args()
    song_page = args.setlist
    sp = Spotify(args.uid)

    create_playlist_from_setlist(sp, args.setlist)
