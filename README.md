# Spotify Artist Discography API

This is a Python-based API built with **FastAPI** that allows you to retrieve the discography of an artist from Spotify. The API communicates with Spotify's web API using the client's credentials to fetch data such as album names, release dates, and total tracks. It follows **SOLID principles** and is designed with testability and maintainability in mind.

### Features

- Search for an artist by name.
- Retrieve the artist's albums, including release dates and track count.
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
git clone https://github.com/yourusername/spotify-artist-discography-api.git
cd spotify-artist-discography-api
```

#### 2. Install dependencies

Make sure you have `python 3.7+` installed. Then, install the dependencies:

```bash
pip install -r requirements.txt
```

#### 3. Set up environment variables

Create a `.env` file in the root directory and add your Spotify credentials:

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

You can obtain your Spotify credentials by registering your application at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

#### 4. Run the API

Start the API server using **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

#### 5. Test the API

You can test the API with a simple HTTP GET request. Example:

```bash
GET http://127.0.0.1:8000/artist/{artist_name}
```

Replace `{artist_name}` with the name of an artist (e.g., `GET http://127.0.0.1:8000/artist/Taylor Swift`).

You can also use the interactive **Swagger UI** at `http://127.0.0.1:8000/docs`.

#### 6. Running Unit Tests

To run the unit tests:

```bash
pytest --maxfail=1 --disable-warnings -q
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

### Folder Structure

```
spotify_api/
│
├── app/
│   ├── __init__.py
│   ├── constants.py          # Stores constant values (API URLs, limits, etc.)
│   ├── models.py             # Pydantic models for request/response validation
│   ├── services.py           # Functions to interact with Spotify API
│   ├── routes.py             # API route definitions
│   ├── main.py               # FastAPI app initialization
│   ├── logger.py             # Logger configuration for error logging
│   └── .env                  # Environment variables (Spotify credentials)
│
├── tests/
│   └── test_spotify.py       # Unit tests for the API
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── requirements.txt          # List of dependencies for Python environment
```

### License

This project is licensed under the MIT License.
