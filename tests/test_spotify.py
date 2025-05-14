from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import pytest
from app.main import app
from app.dependencies.services import get_spotify_service

client = TestClient(app)

@pytest.fixture
def mock_spotify_service():
    mock = MagicMock()
    app.dependency_overrides[get_spotify_service] = lambda: mock
    yield mock
    app.dependency_overrides.clear()

def test_get_artist_discography_success(mock_spotify_service):
    mock_spotify_service.search_artist.return_value = "mock_artist_id"
    mock_spotify_service.get_discography.return_value = [
        {
            "name": "Mock Album",
            "release_date": "2020-01-01",
            "total_tracks": 10,
            "url": "https://spotify.com/mock_album"
        }
    ]

    response = client.get("/artist/MockArtist")
    assert response.status_code == 200
    assert response.json()["artist"] == "MockArtist"
    assert isinstance(response.json()["albums"], list)

def test_get_artist_discography_not_found(mock_spotify_service):
    mock_spotify_service.search_artist.return_value = None

    response = client.get("/artist/UnknownArtist")
    assert response.status_code == 404
    assert response.json()["detail"] == "Artist not found"

def test_search_tracks_success(mock_spotify_service):
    mock_spotify_service.search_tracks.return_value = [
        {
            "name": "Mock Track",
            "artists": [{"name": "Mock Artist"}],
            "album": {"name": "Mock Album"},
            "url": "https://spotify.com/mock_track"
        }
    ]

    response = client.get("/track/MockTrack")
    assert response.status_code == 200
    tracks = response.json()
    assert isinstance(tracks, list)
    assert tracks[0]["name"] == "Mock Track"

def test_search_tracks_not_found(mock_spotify_service):
    mock_spotify_service.search_tracks.return_value = []

    response = client.get("/track/NoTrackFound")
    assert response.status_code == 404
    assert response.json()["detail"] == "No tracks found"
