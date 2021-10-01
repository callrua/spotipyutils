# spotipyutils

Python scripts leveraging the Spotify Web API to offset my laziness when making playlists. 
A wrapper for the Spotify ([spotipy](https://github.com/plamere/spotipy)) API was used 

The following environment variables are required;

```
- SPOTIPY_CLIENT_ID
- SPOTIPY_CLIENT_SECRET
- SPOTIPY_REDIRECT_URI
```

Details around spotipy authorisation can be found [here](http://spotipy.readthedocs.io/en/latest/#authorized-requests) and [here](https://developer.spotify.com/documentation/general/guides/app-settings/)

# Python requirements

python2.7+ 

python-pip packages:

```
spotipy
bs4
```


## Creating a playlist from a setlist.fm link

./utils/setlist_to_spotify.py -u <spotify_user_id> -s <link_to_setlist>

https://www.setlist.fm/setlist/muse/2004/worthy-farm-pilton-england-63d7a6f3.html

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/spotify.png)



## Creating a playlist from user's top tracks 

Creates 3 playlists, top songs based on long term, medium term and short term time period.

./utils/top_tracks_playlist.py -u <spotify_user_id>

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/top_tracks_playlist.png)


## Creating a playlist from a list of genres
./utils/genre_to_playlist.py u <spotify_user_id> -g <list_of_genres> -l <maximum_songs_for_playlist>

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/genre_to_playlist.png)

