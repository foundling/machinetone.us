#!/usr/bin/env python

from flask_frozen import Freezer

from webapp.app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
