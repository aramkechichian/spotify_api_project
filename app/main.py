from fastapi import FastAPI
from .routes.spotify_routes import router

app = FastAPI(title="Spotify Artist Discography API")

app.include_router(router)
