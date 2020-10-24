"""Server for youtube_playlists app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Playlist, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_playlists():

    stats=crud.get_playlists()
    
    playlist_id=[q[0] for q in db.session.query(Playlist.playlist_id).all()]

    channel_name=[q[0] for q in db.session.query(Playlist.channel_name).all()]
           
    playlist_name=[q[0] for q in db.session.query(Playlist.playlist_name).all()]

    number_of_videos=[q[0] for q in db.session.query(Playlist.number_of_videos).all()]

    last_updated=[q[0] for q in db.session.query(Playlist.last_updated).all()]

    return render_template('playlists.html', playlist_id=playlist_id, channel_name=channel_name, playlist_name=playlist_name, number_of_videos=number_of_videos,last_updated=last_updated)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()