#!/usr/bin/env python

def freeze():

    import os
    from flask_frozen import Freezer
    from webapp.app import app

    build_destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
    app.config.update(FREEZER_DESTINATION = build_destination)

    freezer = Freezer(app)

    print(f'building static site to {build_destination} ...') 
    freezer.freeze()
    print('done!') 

if __name__ == '__main__':
    freeze()
