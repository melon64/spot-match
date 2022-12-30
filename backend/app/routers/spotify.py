from pydantic import BaseModel
from fastapi import APIRouter, Header, Depends, HTTPException
from app import config

router = APIRouter()