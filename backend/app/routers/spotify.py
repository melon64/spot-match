from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Header, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import Cookie, Response, Request
from app import config
from app.config import settings
from starlette.middleware.sessions import SessionMiddleware

import time
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
    print(auth_url)
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
    token_info = sp_oauth.get_access_token(code)
    #response.set_cookie(key = "access_token", value = token_info)
    request.session.clear()
    request.session["token_info"] = token_info
    return RedirectResponse(url="/api/spotify/most-played")

#find user's most played song
@router.get("/most-played")
def spotify_most_played(request: Request):
    request.session["token_info"], authorized = get_token(request) 
    if authorized:
        sp = spotipy.Spotify(auth=request.session.get("token_info").get("access_token"))
        results =  sp.current_user_saved_tracks(limit=50)['items']
        return results
    else:
        return {"error": "Not Authorized"}

def get_token(request: Request):
    token_valid = False
    token_info = request.session.get("token_info", None)
    if not (request.session.get("token_info", False)):
        return token_info, token_valid
    
    now = int(time.time())
    is_expired = request.session.get("token_info").get("expires_at") - now < 60
    if is_expired:
        sp_oauth = SpotifyOAuth(
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URI,
            scope=settings.SPOTIFY_SCOPE,
            show_dialog=True
        )
        token_info = sp_oauth.refresh_access_token(request.session.get("token_info").get("refresh_token"))
        request.session["token_info"] = token_info
    return token_info, True



