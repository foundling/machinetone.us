import os
import sqlite3
import sys
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

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

    cur = get_db_cur()
    artists = cur.execute('select * from artist')

    return render_template('artists.html', artists=artists)

@app.route('/artists/<artist_name>')
def artist(artist_name):
    return render_template('artist.html', artist=artist_name)

@app.route('/catalog')
def catalog():

    cur = get_db_cur()
    releases = cur.execute('select * from release').fetchall()

    return render_template('catalog.html', releases=releases)

@app.route('/catalog/<catalog_number>')
def catalog_item(catalog_number):
    statement = """
    select
        artist.name as artist_name,
        release.title as release_title,
        release.catalog_number as catalog_number,
        release.description as release_description,
        release.release_date as release_date,
        release.release_format as release_format
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

# NOTE: make sure to not freeze admin and update stuff.
# this is going to change, using react for front-end in local-only admin panel 
# will possibly return some sort of json
@app.route('/admin')
def admin():

    cur = get_db_cur()

    artists = cur.execute('select id, name from artist').fetchall()
    genres = cur.execute('select id, name from genre').fetchall()
    formats = cur.execute('select id, type from release_format').fetchall()

    today = datetime.strftime(datetime.now(), "%Y-%m-%d")

    return render_template('admin.html', artists=artists, genres=genres, formats=formats, today=today)

@app.route('/update', methods=['POST'])
def update():

    d = request.form.to_dict(flat=False)

    for k,v in d.items():
        print(f"{k}: {','.join(v)}")

    return render_template('update.html')

if __name__ == '__main__':

    app.run(debug=True)
