from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest, Unauthorized

from models import UserModel, EmployeeModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2), "type": user.__class__.__name__}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config('JWT_SECRET'), algorithms=['HS256'])
            return payload['sub'], payload["type"]
        except ExpiredSignatureError:
            raise Unauthorized("token exp")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


auth = HTTPTokenAuth()


@auth.verify_token
def verify(token):

    user_id, user_type = AuthManager.decode_token(token)
    if user_type == "EmployeeModel":
        return EmployeeModel.query.filter_by(id=user_id).first()
    elif user_type == "UserModel":
        return UserModel.query.filter_by(id=user_id).first()
