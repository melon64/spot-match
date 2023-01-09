from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Header, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import Cookie, Response, Request
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
    return RedirectResponse(url=auth_url)

#spotify callback endpoint to get the access and refresh token
@router.get("/callback")
def spotify_callback(code: str, request: Request):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope=settings.SPOTIFY_SCOPE,
        show_dialog=True
    )
    try:
        del request.session["access_token"]
    except:
        pass
    token_info = sp_oauth.get_access_token(code)
    request.session["access_token"] = token_info
    return RedirectResponse(url="/api/spotify/favorite-genres")

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

#find user's favorite genres
@router.get("/favorite-genres")
def spotify_favorite_genres():
    access_token, authorized = get_access_token()
    if authorized:
        sp = spotipy.Spotify(auth=access_token)
        results = sp.current_user_top_artists(limit=50, time_range='short_term')
        genres = []
        for item in results['items']:
            genres.extend(item['genres'])
        return genres
    else:
        return {"error": "Token info not found in cookie"}

#find user's most played song
@router.get("/most-played")
def spotify_most_played():
    access_token, authorized = get_access_token()
    if authorized:
        sp = spotipy.Spotify(auth=access_token)
        results = sp.current_user_top_tracks(limit=10, time_range='short_term')
        return results
    else:
        return {"error": "Token info not found in cookie"}


async def get_access_token(request: Request):
    access_token = None
    authorized = False
    if "access_token" in request.session:
        access_token = request.session["access_token"]
        authorized = True
    return access_token, authorized