
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from .config import settings

from app.routers import auth, user, spotify

app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS"],
#     allow_headers=["Content-Type","Set-Cookie"], 
# )
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(spotify.router, tags=["Spotify"], prefix="/api/spotify")

@app.get("/", tags=["root"])
async def test() -> dict:
    return {"message": "test"}