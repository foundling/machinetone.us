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
def index():
    return render_template('index.html')

@app.route('/artists')
def artists():
    cur = get_db_cur()
    artists = cur.execute('select * from artist')
    return render_template('artists.html', artists=artists)

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/catalog/<release>')
def catalog_item(release):
    return render_template('release.html', release={})

@app.route('/about')
def about():
    return render_template('about.html')


# don't freeze this
@app.route('/admin')
def admin():

    cur = get_db_cur()

    artists = cur.execute('select id, name from artist').fetchall()
    genres = cur.execute('select id, name from genre').fetchall()
    formats = cur.execute('select id, type from release_format').fetchall()

    today = datetime.strftime(datetime.now(), "%Y-%m-%d")

    return render_template('admin.html', artists=artists, genres=genres, formats=formats, today=today)


if __name__ == '__main__':

    app.run(debug=True)
