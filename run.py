#!/usr/bin/env python

from webapp.app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
