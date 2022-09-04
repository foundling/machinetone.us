from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artists')
def artists():
    artists = ["Al's Magic","floodreed"]
    return render_template('artists.html', artists=artists)

@app.route('/catalog')
def catalog():
    releases = ["Cosmic Takes","Chakrat EP"]
    return render_template('catalog.html', releases=releases)

@app.route('/about')
def about():
    return render_template('about.html')


# don't freeze this
@app.route('/admin')
def admin():
    return render_template('admin.html')





if __name__ == '__main__':
    app.run(debug=True)
