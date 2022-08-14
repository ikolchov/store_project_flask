import secrets

from werkzeug.exceptions import NotFound, BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models import UserModel, EmployeeModel
from utils.func_helpers import get_user, get_password, send_mail_credentials


class PasswordManager:

    @staticmethod
    def change_password(data):
        if not data["new_password"] == data["confirm_new_password"]:
            raise ValueError("password does not match")
        user = get_user(data)
        if not check_password_hash(user.password, data["old_password"]):
            raise BadRequest("wrong credentials")
        user.password = generate_password_hash(data["new_password"])
        db.session.commit()
        return "password successfully changed", 202

    @staticmethod
    def reset_password(data):
        user = get_user(data)
        user.password, generated_password = get_password()
        send_mail_credentials(user, generated_password)
        db.session.commit()
        return "password reset check your email", 202




