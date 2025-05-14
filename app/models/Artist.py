from pydantic import BaseModel
from typing import List

class Album(BaseModel):
    name: str
    release_date: str
    total_tracks: int
    url: str

class ArtistDiscographyResponse(BaseModel):
    artist: str
    albums: List[Album]
