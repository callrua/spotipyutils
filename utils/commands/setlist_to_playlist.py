from urllib.request import urlopen
from bs4 import BeautifulSoup


def create_playlist_from_setlist(sp, setlist_url):
    """ Create a Spotify Playlist from a Setlist.fm URL."""
    # Parse the Artist's name from the HTML
    page = urlopen(setlist_url)
    soup = BeautifulSoup(page, 'html.parser')
    artist_name_box = soup.find('div', attrs={'class': 'setlistHeadline'})
    artist_name = artist_name_box.text.strip()
    artist = artist_name.split('Edit venue', 1)[0].rstrip().replace('\n', ' ').replace('Setlist at', '@')

    # Create a blank Spotify playlist
    sp.spotify.user_playlist_create(sp.uid, artist)

    # Parse the setlist's songs from the HTML
    page = urlopen(setlist_url)
    soup = BeautifulSoup(page, 'html.parser')
    songs_html = soup.find_all('a', attrs={'class': 'songLabel'})
    songs = [s.text.strip() for s in songs_html]

    # Add the setlist's songs to the Spotify playlist
    playlists = sp.spotify.user_playlists(sp.uid, limit=1)
    for playlist in playlists['items']:
        for s in songs:
            search_string = s + ' artist:' + artist.split('@ ', 1)[0]
            search_song = sp.spotify.search(q=search_string, type='track', limit=1)
            for song in search_song['tracks']['items']:
                song_uri = song['uri']
                tracks = [song_uri]
                sp.spotify.user_playlist_add_tracks(sp.uid, playlist_id=playlist['id'], tracks=tracks,
                                            position=None)
