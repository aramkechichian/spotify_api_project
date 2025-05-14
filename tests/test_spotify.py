import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

# Mock de funciones para simular respuestas de la API de Spotify
@pytest.fixture
def mock_get_access_token():
    with patch('app.services.get_access_token') as mock:
        yield mock

@pytest.fixture
def mock_search_artist():
    with patch('app.services.search_artist') as mock:
        yield mock

@pytest.fixture
def mock_get_discography():
    with patch('app.services.get_discography') as mock:
        yield mock


def test_get_artist_discography(mock_get_access_token, mock_search_artist, mock_get_discography):
    # Mocking successful access token
    mock_get_access_token.return_value = "valid_token"
    
    # Mocking successful artist search
    mock_search_artist.return_value = "artist_id_123"
    
    # Mocking successful discography fetch
    mock_get_discography.return_value = [
        {"name": "Album 1", "release_date": "2022-01-01", "total_tracks": 10, "url": "spotify_url_1"},
        {"name": "Album 2", "release_date": "2023-01-01", "total_tracks": 12, "url": "spotify_url_2"}
    ]
    
    response = client.get("/artist/Artist Name")
    
    assert response.status_code == 200
    assert response.json() == {
        "artist": "Artist Name",
        "albums": [
            {"name": "Album 1", "release_date": "2022-01-01", "total_tracks": 10, "url": "spotify_url_1"},
            {"name": "Album 2", "release_date": "2023-01-01", "total_tracks": 12, "url": "spotify_url_2"}
        ]
    }

def test_get_artist_not_found(mock_get_access_token, mock_search_artist):
    # Mocking invalid artist search
    mock_get_access_token.return_value = "valid_token"
    mock_search_artist.return_value = None
    
    response = client.get("/artist/Nonexistent Artist")
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Artist not found"}
