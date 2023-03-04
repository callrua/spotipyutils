# spotipyutils

Python scripts leveraging the Spotify Web API to offset my laziness when making playlists. 
A wrapper for the Spotify ([spotipy](https://github.com/plamere/spotipy)) API was used 

# Authentication

You will need to set the tool up in your spotify developer profile to grab your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET.

The following environment variables are also required;

```
- SPOTIPY_CLIENT_ID: Taken from the Spotify Developer Dashboard (detals below)
- SPOTIPY_CLIENT_SECRET: Taken from the Spotify Developer Dashboard (detals below)
- SPOTIPY_REDIRECT_URI: http://localhost/ is sufficient when using spotipy (which we are)
```

Details around spotipy authorisation can be found [here](https://spotipy.readthedocs.io/en/2.19.0/#authorization-code-flow).

When running the app for the first time, the auth from the API will display:

```
Enter the URL you were redirected to:
```

Your preferred browser should pop-up, log in to your Spotify account and then paste the URL it brings you to into your command line, it will look something like:

```
http://localhost/?code=[...]
```

> If using WSL and not seeing a pop-up, try setting the environment variable "BROWSER=wslview"

# Requirements

python3 

python-pip packages can be found in `requirements.txt`

# Building

### Docker:

```
docker build --build-arg SPOTIPY_CLIENT_ID=<spotify_client_id> --build-arg SPOTIPY_CLIENT_SECRET=<spotify_client_secret>
3d3583f4f1 --build-arg SPOTIPY_REDIRECT_URI=<spotify_redirect_uri> -t spotipy_image --rm .
```

### pip with setup.py

```
pip install --editable .
```

## Creating a playlist from a setlist.fm link

```
docker run spotipy_image setlist_to_playlist --setlist <setlist.fm_url> --id <spotify_user_id>
```

```
spotipy-utils setlist_to_playlist --setlist <setlist.fm_url> --id <spotify_user_id>
```

https://www.setlist.fm/setlist/muse/2004/worthy-farm-pilton-england-63d7a6f3.html

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/spotify.png)



## Creating a playlist from user's top tracks 

Creates 3 playlists, top songs based on long term, medium term and short term time period.

```
docker run spotipy_image top_tracks_to_playlist --id <spotify_user_id> 
```

```
spotipy-utils top_tracks_to_playlist --id <spotify_user_id>
```

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/top_tracks_playlist.png)


## Creating a playlist from a list of genres
./utils/genre_to_playlist.py u <spotify_user_id> -g <list_of_genres> -l <maximum_songs_for_playlist>

![alt text](https://github.com/callrua/setlistToSpotify/blob/master/screencaps/genre_to_playlist.png)

