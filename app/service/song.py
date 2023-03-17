from typing import Dict, List, Tuple

from app import db
from app.model import Song


def save_new_song(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    """save new song object in database

    Args:
        data (Dict[str, str, int]): Dictionary with interpret, title and length

    Returns:
        Tuple[Dict[str, str, int], int]: the response object and a status code
    """

    song = Song.query.filter_by(
        title=data["title"], interpret=data["interpret"]
    ).first()
    if not song:
        new_song = Song(
            interpret=data["interpret"], title=data["title"], length=data["length"]
        )
        save_changes(song=new_song)
        response_object = {"status": "success", "message": "Successfully added song."}
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Song already exists",
        }
        return response_object, 409


def get_all_songs() -> Song:
    """get all songs

    Returns:
        [Song]: a list of all songs
    """
    return Song.query.all()


def save_changes(song: Song) -> None:
    """save song to database


    Args:
    song (Song): the song object
    """

    db.session.add(song)
    db.session.commit()


def get_length_by_title(title: str, interpret: str) -> Song:
    """get length by title

    Args:
        title (str): the title
        interpret (str): the interpret

    Returns:
        song (Song): the song object
    """
    return Song.query.filter_by(title=title, interpret=interpret).first()


def get_song_by_id(id: int) -> Song:
    """get song by id

    Args:
        id (int): the id

    Returns:
        [Song]: the song object
    """
    return Song.query.filter_by(id=id).first()


def delete_song(song: Song) -> None:
    """delete song

    Args:
        song (Song): the song object
    """
    db.session.delete(song)
    db.session.commit()


def update_song(song: Song, data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    """update song

    Args:
        song (Song): the song object

    Returns:
        Tuple[Dict[str, str, int], int]: the response object and a status code
    """

    song.interpret = data["interpret"]
    song.title = data["title"]
    song.length = data["length"]
    db.session.commit()
    response_object = {"status": "success", "message": "Successfully updated song."}
    return response_object, 201
