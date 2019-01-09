# SpotifyUtils

This repo is dedicated to utility scripts created for Spotify using the Spotify Web API. A python wrapper spotipy was used (details [here](https://github.com/plamere/spotipy))

The following environment variables are required;
- SPOTIPY_CLIENT_ID
- SPOTIPY_CLIENT_SECRET
- SPOTIPY_REDIRECT_URI

Details around spotipy authorisation can be found [here](http://spotipy.readthedocs.io/en/latest/#authorized-requests)

## SetlistToSpotify

From ./utils/setlist_to_spotify.py

Take a setlist from setlist.fm and creates a Spotify playlist

https://www.setlist.fm/setlist/muse/2004/worthy-farm-pilton-england-63d7a6f3.html

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/spotify.png)

usage; -u <spotify_user_id> -s <link_to_setlist>

Dependencies;

- pip install spotipy
- pip install bs4



## Playlist by Genre
From ./utils/genre_to_playlist.py

Create a spotify playlist based on a list of genres.

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/genre_to_playlist.png)

usage; -u <spotify_user_id> -g <list_of_genres> -l <maximum_songs_for_playlist>
