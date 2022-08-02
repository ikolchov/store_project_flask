from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest

from models import UserModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")


    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, key=config('JWT_SECRET'), algorithms=['HS256'])
            return payload['sub']
        except ExpiredSignatureError:
            return BadRequest("token exp")
        except InvalidTokenError:
            return BadRequest("Invalid Token")


auth = HTTPTokenAuth()

@auth.verify_token
def verify(token):
    user_id = AuthManager.decode_token(token)
    return UserModel.query.filter_by(id=user_id).first
