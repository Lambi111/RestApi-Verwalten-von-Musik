from flask import request
from flask_restx import Resource
from typing import Dict, Tuple

from ..dto.song import SongDto
from ..service.song import save_new_song, get_all_songs, get_length_by_title, delete_song

api = SongDto.api
_song = SongDto.song

@api.route("/")
class SongList(Resource):
    """route to all songs and create a new song
    
    Args:
        Ressource (UserDto.song): the song dto

    Returns:
        [Book]: List of songs
    """

    @api.doc("list_of_songs")
    @api.marshal_list_with(_song, envelope="data")
    def get(self):
        """List all songs"""
        return get_all_songs()
    
    @api.expect(_song, validate=True)
    @api.response(201, "Song succesfully created.")
    @api.doc("create a new song")
    def post(self) -> Tuple[Dict[str, str], int]:
        """post route to cretae new song
        
        Returns:
            Tuple[Dict[int, str, str, int], int]: response and status
        """

        data = request.json
        return save_new_song(data=data)
    
    @api.response(201, "Song succesfully deleted.")
    @api.doc("delete song")
    def delete(self):
        """delete route to delete a song
        
        Args: 

        """

        data = request.json
        return delete_song(data=data)
    
@api.route("/<title>")
@api.param("title", "The song title")
@api.response(404, "Song not found.")
class Song(Resource):
    """route to get length by title
    
    Args:
        Resource (str): title

    Returns:
        [length]: the length
    """
    

    @api.doc("get the length")
    @api.marshal_with(_song)
    def get(self, title: str):
        """get the length 
        
        Args:
            title (str): the title

        Returns:
            [length]: the length
        """
        song = get_length_by_title(title=title)
        if not song:
            api.abort(404)
        else:
            return song


