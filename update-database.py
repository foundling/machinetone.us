#!/usr/bin/env python

import os

from dotenv import load_dotenv
import gspread

load_dotenv()

service_account = gspread.service_account(filename='service_account.json')

# googlesheet name is 'Machine Tone Database'
sheet = service_account.open_by_key(os.getenv('MT_GOOGLESHEETS_DB_ID'))
artist_worksheet = sheet.worksheet('Artist')
release_worksheet = sheet.worksheet('Release')

(artist_header, *artists) = artist_worksheet.col_values(1)
(release_header, *releases) = release_worksheet.col_values(1)

print(artist_header)
print(artists)

print(release_header)
print(releases)

