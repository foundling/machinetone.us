# Machine Tone Website

## Architecture

This site is intended to be developed locally, built as a static site and deployed as static pages to the cloud.  No live database is involved in the end product.

- SQLite3 database (`webapp/db/mt.db`) for MT artist/release/etc data
- A Flask app (`webapp/app.py`, run via `run.py`) for rendering data-backed site pages
    - runs on `localhost:5000` when you run `./run.py`
    - has `/api/<resource>` routes that serve JSON to the admin front-end
- Frozen-Flask for generating an easily-deployable static site from the Flask App (`freeze.py`)
- A cli for building the static site and deploying it to the cloud (`mt.py`)
- A React frontend application for local-only database modifications like creating new releases, editing data (`mt-admin`)
    - runs on `localhost:3000` when you `cd` to `mt-admin/` and run `npm run start`
