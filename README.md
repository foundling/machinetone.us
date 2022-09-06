# Machine Tone Website

## Architecture

- SQLite3 database (`webapp/db/mt.db`) for MT artist/release/etc data
- A Flask app (`webapp/app.py`, run via `run.py`) for rendering data-backed site pages
    - runs on `localhost:5000`
    - has `/api/<resource>` routes that serve JSON to the admin front-end
- Frozen-Flask for generating an easily-deployable static site from the Flask App (`freeze.py`)
- A cli for building the static site and deploying it to the cloud (`mt.py`)
- React front-end for a local-only admin panel to modify database stuff like creating new releases, editing data (`mt-admin`)
    - runs on `localhost:3000`
