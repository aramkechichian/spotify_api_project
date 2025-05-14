from pydantic import BaseModel
from typing import List

class SongArtist(BaseModel):
    name: str

class SongAlbum(BaseModel):
    name: str

class SongSearchResponse(BaseModel):
    name: str
    artists: List[SongArtist]
    album: SongAlbum
    url: str