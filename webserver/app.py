from flask import Flask, render_template, request
from utils.genre_to_playlist import GenreToPlaylist
from flask_navigation import Navigation

app = Flask(__name__)
app.secret_key = 'super secret key'
nav = Navigation(app)

# initializing Navigations
nav.Bar('top', [
    nav.Item('Genre 2 Playlist', 'genre2playlist'),
])

g2p = GenreToPlaylist("11178142667")
GENRES = g2p.get_genres()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/genre_to_playlist', methods=['GET', 'POST'])
def genre2playlist():
    if request.method == 'POST':
        _genres = []
        for genre in GENRES:
            if request.form.get(genre):
                _genres.append(genre.lower())
        limit = request.form['limit']
        g2p.generate_playlist(_genres, limit)
        return render_template('genreToPlaylist.html', genres=GENRES)
    else:
        return render_template('genreToPlaylist.html', genres=GENRES)
