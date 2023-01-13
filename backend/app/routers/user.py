from fastapi import APIRouter, Depends, Request
from bson.objectid import ObjectId
from app.serializers.userSerializers import userResponseEntity, userListEntity

from app.database import User
from .. import schemas, oauth2

router = APIRouter()


@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}

@router.get('/matches', response_model=schemas.UserListResponse)
def get_matches(user_id: str = Depends(oauth2.require_user)):
    users = User.find({}).limit(5)
    users = [user for user in users if str(user['_id']) != user_id]
    users = userListEntity(users)
    return {"status": "success", "users": users}

#edit user playlist
@router.put('/playlist', response_model=schemas.UserResponse)
def edit_playlist(user_id: str = Depends(oauth2.require_user), payload: schemas.UserBaseSchema = Depends()):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    user['playlist'] = payload.playlist
    User.update_one({'_id': ObjectId(str(user_id))}, {'$set': user})
    return {"status": "success", "user": user}

#view other user profile by id
@router.get('/user/{user_id}', response_model=schemas.UserResponse)
def get_user(user_id: str):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}