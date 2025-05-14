from fastapi import APIRouter, HTTPException, Depends
from ..dependencies.services import get_spotify_service
from ..services.spotify_services import SpotifyService
from ..models.Artist import ArtistDiscographyResponse
from ..models.Song import SongSearchResponse
router = APIRouter()

@router.get("/artist/{artist_name}", response_model=ArtistDiscographyResponse)
def get_artist_discography(artist_name: str, spotify_service: SpotifyService = Depends(get_spotify_service)) -> ArtistDiscographyResponse:
    artist_id = spotify_service.search_artist(artist_name)
    if not artist_id:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    albums = spotify_service.get_discography(artist_id)
    return ArtistDiscographyResponse(artist=artist_name, albums=albums)


@router.get("/track/{track_name}", response_model=list[SongSearchResponse])
def search_tracks(track_name: str, spotify_service: SpotifyService = Depends(get_spotify_service)) -> list[SongSearchResponse]:
    tracks = spotify_service.search_tracks(track_name)
    if not tracks:
        raise HTTPException(status_code=404, detail="No tracks found")
    return tracks