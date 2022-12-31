from pydantic import BaseModel
from fastapi import APIRouter, Header, Depends, HTTPException
from app import config
from app.config import settings

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyAuth(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str


router = APIRouter()

@router.get("/login")
def spotify_login():
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope=settings.SPOTIFY_SCOPE,
        show_dialog=True
    )
    auth_url = sp_oauth.get_authorize_url()
    return {"status": "success", "auth_url": auth_url}

#spotify callback endpoint to get the access and refresh token
@router.get("/callback")
def spotify_callback(code: str):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope=settings.SPOTIFY_SCOPE,
        show_dialog=True
    )
    token_info = sp_oauth.get_access_token(code)
    return token_info

#refresh the access token
@router.get("/refresh")
def spotify_refresh_token(refresh_token: str):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope=settings.SPOTIFY_SCOPE,
        show_dialog=True
    )
    token_info = sp_oauth.refresh_access_token(refresh_token)
    return token_info

#find user's top artists
@router.get("/top-artists")
def spotify_top_artists(access_token: str):
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_top_artists(limit=50, time_range='short_term')
    return results

#find user's top tracks
@router.get("/top-tracks")
def spotify_top_tracks(access_token: str):
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_top_tracks(limit=50, time_range='short_term')
    return results

#find user's favorite genres
@router.get("/favorite-genres")
def spotify_favorite_genres(access_token: str):
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_top_artists(limit=50, time_range='short_term')
    genres = []
    for item in results['items']:
        genres.extend(item['genres'])
    return genres
