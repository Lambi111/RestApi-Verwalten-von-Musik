from .. import db


class Song(db.Model):
    """Song Model for storing song related details"""

    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interpret = db.Column(db.String(250))
    title = db.Column(db.String(250))
    length = db.Column(db.Integer)
