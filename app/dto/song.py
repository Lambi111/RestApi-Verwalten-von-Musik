from flask_restx import Namespace, fields

class SongDto:
    """The song dto"""

    api = Namespace("song", description="song related operations")
    song = api.model(
        "song",
        {
            "id": fields.Integer(required=True, description="song id"),
            "interpret": fields.String(required=True, description="song interpret"),
            "title": fields.String(required=True, description="song title"),
            "length": fields.Integer(required=True, description="song length"),
        },
    )