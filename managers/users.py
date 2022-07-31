from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import UserModel


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)

    @staticmethod
    def login(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("You are not logged in!")
        if check_password_hash(user.password, user_data["password"]):
            return AuthManager.encode_token(user)
        raise BadRequest("Wrong Password!")
