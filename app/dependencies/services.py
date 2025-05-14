from app.services.spotify_services import SpotifyService

def get_spotify_service() -> SpotifyService:
    return SpotifyService()