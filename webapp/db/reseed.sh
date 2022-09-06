#!/usr/bin/env bash

[ -f mt.db ] && \mv mt.db mt.db.bak
sqlite3 mt.db < mt.sqlite

