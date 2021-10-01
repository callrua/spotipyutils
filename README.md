# spotipyutils

Python scripts leveraging the Spotify Web API to offset my laziness when making playlists. 
A wrapper for the API was used ([spotipy](https://github.com/plamere/spotipy))

The following environment variables are required;

```
- SPOTIPY_CLIENT_ID
- SPOTIPY_CLIENT_SECRET
- SPOTIPY_REDIRECT_URI
```

Details around spotipy authorisation can be found [here](http://spotipy.readthedocs.io/en/latest/#authorized-requests) and [here](https://developer.spotify.com/documentation/general/guides/app-settings/)

# Python requirements

python-pip:

```
spotipy
bs4
```


## Creating a playlist from a setlist.fm link

./utils/setlist_to_spotify.py

https://www.setlist.fm/setlist/muse/2004/worthy-farm-pilton-england-63d7a6f3.html

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/spotify.png)

usage; -u <spotify_user_id> -s <link_to_setlist>


## Creating a playlist from user's top tracks 

Creates 3 playlists, top songs based on long term, medium term and short term time period.

./utils/top_tracks_playlist.py

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/top_tracks_playlist.png)

usage; -u <spotify_user_id>

## Creating a playlist from a list of genres
From ./utils/genre_to_playlist.py

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/genre_to_playlist.png)

usage; -u <spotify_user_id> -g <list_of_genres> -l <maximum_songs_for_playlist>
