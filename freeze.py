#!/usr/bin/env python


def freeze():

    import os
    from flask_frozen import Freezer
    import sqlite3
    from webapp.app import app, get_db_cur

    # Freezer config
    build_destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
    app.config.update(FREEZER_DESTINATION = build_destination)
    app.config.update(FREEZER_REMOVE_EXTRA_FILES = True)

    freezer = Freezer(app)

    # /catalog/<catalog_item>
    @freezer.register_generator
    def catalog_item():

        cur = get_db_cur()
        catalog_numbers = cur.execute('select catalog_number from release order by catalog_number desc').fetchall()

        for result in catalog_numbers:
            yield { 'catalog_number': result['catalog_number'] }

    freezer.freeze()

if __name__ == '__main__':
    freeze()
