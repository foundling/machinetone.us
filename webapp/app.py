from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artists')
def artists():
    artists = ["Al's Magic","floodreed"]
    return render_template('artists.html', artists=artists)

@app.route('/releases')
def releases():
    releases = ["Cosmic Takes","Chakrat EP"]
    return render_template('releases.html', releases=releases)

# don't freeze this
@app.route('/admin')
def admin():
    return render_template('admin.html')





if __name__ == '__main__':
    app.run(debug=True)
