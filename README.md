# Machine Tone Website

## Architecture

- SQLite3 database (`webapp/db/mt.db`) for MT artist/release/etc data
- A Flask app (`webapp/app.py`) for rendering data-backed site pages
- Frozen-Flask for generating an easily-deployable static site from the Flask App (`freeze.py`)
- A cli for building and pushing static site to the cloud (`mt.py`)
- React front-end for a local-only admin panel to modify database stuff like creating new releases, editing data (`mt-admin`)
