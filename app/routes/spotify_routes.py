from fastapi import APIRouter, HTTPException
from ..services.spotify_services import SpotifyService
from ..models.Artist import ArtistDiscographyResponse

router = APIRouter()

@router.get("/artist/{artist_name}", response_model=ArtistDiscographyResponse)
def get_artist_discography(artist_name: str) -> ArtistDiscographyResponse:
    spotify_service = SpotifyService()
    artist_id = spotify_service.search_artist(artist_name)
    if not artist_id:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    albums = spotify_service.get_discography(artist_id)
    return ArtistDiscographyResponse(artist=artist_name, albums=albums)
