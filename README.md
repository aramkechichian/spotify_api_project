# Spotify API

This is a Python-based API built with **FastAPI** that allows you to retrieve the discography of an artist, and list of songs from Spotify. The API communicates with Spotify's web API using the client's credentials to fetch data such as album names, release dates, and total tracks. It follows **SOLID principles** and is designed with testability and maintainability in mind.

### Features

- Search for an artist by name.
- Retrieve the artist's albums, including release dates and track count.
- Search for an songs list by name.
- RESTful API with clear error handling.
- Unit tests with `pytest`.
- Authentication with Spotify using the **Client Credentials Flow**.

### Technologies Used

- **FastAPI**: For building the API.
- **Pydantic**: For data validation and serialization.
- **Requests**: For HTTP requests to Spotify API.
- **Logging**: For error logging.
- **Pytest**: For testing the application.

### Setup

#### 1. Clone the repository

```bash
git clone https://github.com/aramkechichian/spotify-artist-discography-api.git
cd spotify-artist-discography-api
```

#### 2. Set up environment variables

Create a `.env` file in the root directory and add your Spotify credentials:

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

You can obtain your Spotify credentials by registering your application at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

#### 3. Install dependencies and run the API

Make sure you have `python 3.7+` installed. Then, install the dependencies with the dev.sh script:

```bash
Available Commands:
./dev.sh init     # Create virtual environment, install dependencies, and start the app
./dev.sh run      # Start the app (requires environment to be already set up)
./dev.sh test     # Run tests using pytest
./dev.sh stop     # Display message to manually stop the app (Ctrl+C)
./dev.sh clear    # Remove the virtual environment
```
The API will be available at `http://127.0.0.1:8000`.

#### 4. Test the API

You can test the API with a simple HTTP GET request. Example:

```bash
GET http://127.0.0.1:8000/artist/{artist_name}
```

Replace `{artist_name}` with the name of an artist (e.g., `GET http://127.0.0.1:8000/artist/Taylor Swift`).

You can also use the interactive **Swagger UI** at `http://127.0.0.1:8000/docs`.

#### 5. Running Unit Tests

To run the unit tests:

```bash
./dev.sh test
```

This will run all the tests defined in the `tests/` directory.

### API Endpoints

#### `GET /artist/{artist_name}`

- **Description**: Retrieves the discography of the specified artist.
- **Parameters**: 
  - `artist_name`: Name of the artist (e.g., "Taylor Swift").
- **Response**: 
  - 200 OK: Returns the artist's albums with details like name, release date, total tracks, and a URL to the album on Spotify.
  - 404 Not Found: If the artist cannot be found.
  - 500 Internal Server Error: If there's an error during the API request.

#### `GET /track/{track_name}`

- **Description**: Retrieves the list of songs.
- **Parameters**: 
  - `track_name`: Name of the song (e.g., "Bohemian Rhapsody").
- **Response**: 
  - 200 OK: Returns the song's lits with details like name, album, and a URL to the song on Spotify.
  - 404 Not Found: If the song cannot be found.
  - 500 Internal Server Error: If there's an error during the API request.

### Folder Structure

```
spotify_api/
│
├── app/
│   ├── __init__.py              # Initializes the app package
│   ├── constants.py             # Stores constant values (API URLs, limits, etc.)
│   ├── models/                  # Pydantic models for request/response validation
│   │   └── __init__.py          # Pydantic model definitions
│   │   └── Artist.py            # Specific models for Spotify Artist data
│   │   └── Song.py              # Specific models for Spotify Song data
│   ├── services/                # Functions to interact with Spotify API
│   │   └── __init__.py          # Initialize services module
│   │   └── spotify_service.py   # Functions for Spotify interactions
│   ├── routes/                  # API route definitions
│   │   └── __init__.py          # Initialize routes module
│   │   └── spotify_routes.py    # Define routes for Spotify API
│   ├── main.py                  # FastAPI app initialization
│   ├── logger.py                # Logger configuration for error logging
│   └── .env                     # Environment variables (Spotify credentials)
│
├── tests/
│   └── test_spotify.py          # Unit tests for the API
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore file for ignoring unnecessary files

```
### License

This project is licensed under the MIT License.
