from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artists')
def artists():
    print(request.endpoint)
    artists = ["Al's Magic","floodreed"]
    return render_template('artists.html', artists=artists, endpoint=request.endpoint)

@app.route('/catalog')
def catalog():
    releases = ["Cosmic Takes","Chakrat EP"]
    return render_template('catalog.html', releases=releases, endpoint=request.endpoint)

@app.route('/about')
def about():
    return render_template('about.html', endpoint=request.endpoint)


# don't freeze this
@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
