from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from app.serializers.userSerializers import userResponseEntity

from app.database import User
from .. import schemas, oauth2

router = APIRouter()


@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    return {"status": "success", "user": user}


#return list of all users with only id and name
# @router.get('/all', response_model=schemas.UserListResponse)
# def get_all_users():
#     users = User.find({})
#     users = [userResponseEntity(user) for user in users]
#     return {"status": "success", "users": users}

# #view other user profile by id
# @router.get('/{user_id}', response_model=schemas.UserResponse)
# def get_user(user_id: str):
#     user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
#     return {"status": "success", "user": user}