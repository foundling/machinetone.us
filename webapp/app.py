import os
import sqlite3
import sys
from datetime import datetime

from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

def get_db_cur():

    db_path = os.path.join(os.path.dirname(__file__), 'db', 'mt.db')
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row

    return con.cursor()

@app.route('/')
def home():
    cur = get_db_cur()
    statement = """
    select 
        artist.name as artist_name,
        release.catalog_number as catalog_number,
        release.title as release_title,
        release.release_date as release_date,
        release.description as release_description
    from
        artist
    join
        release
    on
        artist.id = release.artist_id
    order by
        release_date desc
    limit 1;
    """
    latest_release = cur.execute(statement).fetchone()
    return render_template('index.html', latest_release=latest_release)

@app.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/artists')
def artists():

    statement = """
    select
        artist.name as artist_name,
        artist.bio as artist_bio,
        artist.id as id
    from
        artist
    order by artist_name asc;
    """
    cur = get_db_cur()
    artists = cur.execute(statement).fetchall()

    return render_template('artists.html', artists=artists)

@app.route('/artists/<artist_id>')
def artist(artist_id):
    statement = """
    select
        name as artist_name,
        id as artist_id,
        bio as artist_bio,
        url as artist_url
    from
        artist
    where
        artist_id = ?
    """
    cur = get_db_cur()
    artist = cur.execute(statement, [artist_id]).fetchone()
    return render_template('artist.html', artist=artist)

@app.route('/catalog')
def catalog():

    cur = get_db_cur()
    statement = """
    select
        release.catalog_number,
        release.title, 
        release.release_date,
        release.description,
        artist.name as artist,
        release_format.format,
        release_medium.medium
    from
        release
    join
        artist on artist.id = release.artist_id
    join
        release_format on release_format.id = release.release_format
    join
        release_medium on release_medium.id = release.release_medium;
    """

    releases = cur.execute(statement).fetchall()
    print([dict(release) for release in releases])

    return render_template('catalog.html', releases=releases)

@app.route('/catalog/<catalog_number>')
def catalog_item(catalog_number):
    statement = """
    select
        artist.name as artist,
        release.title as title,
        release.catalog_number as catalog_number,
        release.description as description,
        release.release_date as release_date,
        release.release_format as format
    from
        release
    join
        artist on artist.id = release.artist_id
    where
        release.catalog_number = ?;
    """
    cur = get_db_cur()
    release = cur.execute(statement, [catalog_number.upper()]).fetchone();
    print(release)
    return render_template('release.html', release=release)


## API FOR LOCAL-ONLY ADMIN PANEL

@app.route('/api/artists', methods=['GET', 'POST'])
def api_artists():

    cur = get_db_cur()
    artists = cur.execute('select * from artist').fetchall();

    return {
        "artists": [
            dict(artist) for artist in artists
        ]
    }

if __name__ == '__main__':

    app.run(debug=True)
