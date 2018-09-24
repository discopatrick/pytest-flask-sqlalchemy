import os

from flask import escape, Flask

from flaskapp.database import db_session
from flaskapp.models import Thing


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def things():
        thing = Thing(name='another thing')
        db_session.add(thing)
        db_session.commit()

        all_the_things = db_session.query(Thing).all()

        return escape(str(all_the_things))

    return app
