import requests
from ..constants import SPOTIFY_API_BASE_URL, SPOTIFY_TOKEN_URL, SPOTIFY_GRANT_TYPE, SPOTIFY_LIMIT
from ..logger import logger
import os
from fastapi import HTTPException
from app.models.Artist import Album
from app.models.Song import SongSearchResponse, SongArtist, SongAlbum 

class SpotifyService:
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.client_id = client_id or os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("SPOTIFY_CLIENT_SECRET")
        if not self.client_id or not self.client_secret:
            raise ValueError("Spotify client ID and secret must be provided")
        self.token = self.get_access_token()

    def get_access_token(self) -> str:
        try:
            response = requests.post(
                SPOTIFY_TOKEN_URL,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={"grant_type": SPOTIFY_GRANT_TYPE},
                auth=(self.client_id, self.client_secret)
            )
            response.raise_for_status()
            return response.json().get("access_token")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching access token: {e}")
            raise Exception("Unable to authenticate with Spotify API")

    def search_artist(self, artist_name: str) -> str:
        if not self.token:
            raise HTTPException(status_code=500, detail="Unable to authenticate with Spotify")
        url = f'{SPOTIFY_API_BASE_URL}/search'
        headers = {'Authorization': f'Bearer {self.token}'}
        params = {'q': artist_name, 'type': 'artist', 'limit': 1}
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            items = response.json().get('artists', {}).get('items', [])
            if not items:
                return None
            return items[0]['id']
        except requests.exceptions.RequestException as e:
            logger.error(f"Error searching artist: {e}")
            raise Exception("Error while searching for artist")

    def get_discography(self, artist_id: str) -> list[Album]:
        url = f'{SPOTIFY_API_BASE_URL}/artists/{artist_id}/albums'
        headers = {'Authorization': f'Bearer {self.token}'}
        params = {'include_groups': 'album,single', 'limit': SPOTIFY_LIMIT}
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            albums = response.json().get('items', [])
            unique_albums = {album['name']: album for album in albums}.values()
            return [
                Album(
                    name=album['name'],
                    release_date=album['release_date'],
                    total_tracks=album['total_tracks'],
                    url=album['external_urls']['spotify']
                )
                for album in unique_albums
            ]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching discography: {e}")
            raise HTTPException(status_code=500, detail="Error fetching artist discography")

    def search_tracks(self, track_name: str) -> list[SongSearchResponse]:
        if not self.token:
            raise HTTPException(status_code=500, detail="Unable to authenticate with Spotify")
        url = f"{SPOTIFY_API_BASE_URL}/search"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {"q": track_name, "type": "track", "limit": 10}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            items = response.json().get("tracks", {}).get("items", [])
            if not items:
                return []

            return [
                SongSearchResponse(
                    name=track["name"],
                    artists=[SongArtist(name=artist["name"]) for artist in track["artists"]],
                    album=SongAlbum(name=track["album"]["name"]),
                    url=track["external_urls"]["spotify"]
                )
                for track in items
            ]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error searching tracks: {e}")
            raise HTTPException(status_code=500, detail="Error while searching for tracks")