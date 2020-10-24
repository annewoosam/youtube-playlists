"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb youtube_playlists')

os.system('createdb youtube_playlists')

model.connect_to_db(server.app)

model.db.create_all()


# Create playlist table's initial data.

with open('data/playlist.json') as f:

    playlist_data = json.loads(f.read())

playlist_in_db = []

for playlist in playlist_data:
    channel_name, playlist_name, number_of_videos, last_updated (
                                   playlist['channel_name'],
                                   playlist['playlist_name'],
                                   playlist['number_of_videos,
                                   playlist['last_updated'])

    db_playlist = crud.create_playlist(
                                 channel_name,
                                 playlist_name,
                                 number_of_videos,
                                 last_updated)

    playlist_in_db.append(db_playlist)
