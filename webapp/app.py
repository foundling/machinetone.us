import os
import sqlite3

from flask import Flask, render_template, request
import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artists')
def artists():
    return render_template('artists.html')

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
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
