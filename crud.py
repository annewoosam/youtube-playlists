"""CRUD operations."""

from model import db, Playlist, connect_to_db

import datetime


def create_playlist(channel_name, playlist_name, number_of_videos, last_updated):
   

    playlist = Playlist(channel_name=channel_name,
                  playlist_name=playlist_name,
                  number_of_videos=number_of_videos,
                  last_updated=last_updated)

    db.session.add(playlist)

    db.session.commit()

    return playlist

def get_playlist():
    """Return all rows of playlist monthly data."""

    return Playlist.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
