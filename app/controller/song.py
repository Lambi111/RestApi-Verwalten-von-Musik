from flask import request
from flask_restx import Resource
from typing import Dict, Tuple

from ..dto.song import SongDto
from ..service.song import (
    save_new_song,
    get_all_songs,
    get_length_by_title,
    delete_song,
    get_song_by_id,
    update_song,
)

api = SongDto.api
_song = SongDto.song
_song_post = SongDto.song_post
_song_info = SongDto.song_info


@api.route("/")
class SongList(Resource):
    """route to all songs and create a new song

    Args:
        Ressource (UserDto.song): the song dto

    Returns:
        [Song]: List of songs
    """

    @api.doc("list_of_songs")
    @api.marshal_list_with(_song, envelope="data")
    def get(self):
        """List all songs"""
        return get_all_songs()

    @api.expect(_song_post, validate=True)
    @api.response(201, "Song succesfully created.")
    @api.doc("create a new song")
    def post(self) -> Tuple[Dict[str, str], int]:
        """create new song

        Returns:
            Tuple[Dict[str, str], int]: response and status
        """

        data = request.json
        return save_new_song(data=data)


@api.route("/<id>")
@api.param("id", "The song id")
class Song(Resource):
    """route to delete song by id

    Args:
        Resource (int): id
    """

    @api.response(201, "Song succesfully deleted.")
    @api.doc("delete the song by the id")
    @api.marshal_list_with(_song)
    def delete(self, id: int):
        """delete the song by id

        Args:
            id (int): the id
        """
        song = get_song_by_id(id=id)
        if not song:
            api.abort(404, "Song not found")
        else:
            return delete_song(song)

    @api.expect(_song_post, validate=True)
    @api.doc("update a song")
    @api.response(201, "Song succesfully updated")
    def put(self, id: int) -> Tuple[Dict[str, str], int]:
        """update a song

        Args:
             id (int): the id

        Returns:
            [Song]: the new song object
        """
        data = request.json
        song = get_song_by_id(id=id)
        if not song:
            api.abort(404, "Song not exists")
        else:
            return update_song(song, data=data)


@api.route("/<title>/<interpret>")
@api.param("title", "The song title", "interpret" "The song interpret")
@api.response(404, "Song not found.")
class Length(Resource):
    """route to get length by title

    Args:
        Resource (str): title, interpret

    Returns:
        length (int): the length
    """

    @api.doc("get the length")
    @api.marshal_list_with(_song_info, envelope="data")
    def get(self, title: str, interpret: str):
        """get the length

        Args:
            title (str): the title

        Returns:
            [Song]: the new song object
        """
        return get_length_by_title(title=title, interpret=interpret)
