# spotipyutils

Python scripts leveraging the Spotify Web API to offset my laziness when making playlists. 
A wrapper for the Spotify ([spotipy](https://github.com/plamere/spotipy)) API was used 

You will need to set the tool up in your spotify developer profile to grab your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET.

The following environment variables are required;

```
- SPOTIPY_CLIENT_ID: Taken from the Spotify Developer Dashboard (detals below)
- SPOTIPY_CLIENT_SECRET: Taken from the Spotify Developer Dashboard (detals below)
- SPOTIPY_REDIRECT_URI: http://localhost/ is sufficient when using spotipy (which we are)
```

Details around spotipy authorisation can be found [here](http://spotipy.readthedocs.io/en/latest/#authorized-requests).

When running the app for the first time, the auth from the API will display:

```
Enter the URL you were redirected to:
```

Your preferred browser should pop-up, log in to your Spotify account and then paste the URL it brings you to into your command line, it will look something like:

```
http://localhost/?code=[...]
```

# Python requirements

python3 

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

