from typing import Dict, List, Tuple

from app import db
from app.model import Song

def save_new_song(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    """save new song object in database
    
    Args:
        data (Dict[str, str, str]): Dictionary with id, title, interpret and length

    Returns: 
        Tuple[Dict[str, str, str], int]: the response object and a status code
    """

    song = Song.query.filter_by(id=data["id"]).first()
    if not song:
        new_song = Song(id=data["id"], interpret=data["interpret"], titel=data["title"], length=data["length"])
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

def get_length_by_title(title: str) -> Song:
    """get length by title
    
    Args:
        title (str): the title
            
    Returns:
        [length]: the length             
    """
    return Song.query.filter_by(title=title).first()


def get_song_by_id(id: int) -> Song:
    """get song by id
    
    Args:
        id (int): the id

    Return:
        [Song]: the song object    
    """
    return Song.query.filter_by(id=id).first()


def delete_song():
    """delete song

    Args: 
        song (Song): the song object
    """
    song = get_song_by_id
    db.session.delete(song)
    db.session.commit()


def update_song(data: Dict [str, str]) -> Tuple[Dict[str, str], int]:
    """update a book in database
    
    Args: 
        data (Dict[str, str]): Dictionary with id, title, interpret and length

    Returns:
        Tuple[Dict[str, str], int]: the response object and a status code
    """

    song = get_song_by_id
    new_song = Song(id=data["id"], interpret=data["interpret"], titel=data["title"], length=data["length"])
    response_object = {"status": "success", "message": "Successfully updated song."}
    return response_object, 201

    
