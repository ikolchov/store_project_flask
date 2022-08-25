from marshmallow import Schema, fields, validates
from werkzeug.exceptions import BadRequest, Conflict

from models import UserModel
from utils.func_helpers import get_password_strength


class UserSignInSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    password = fields.String(required=True)

    @validates("password")
    def validate_password(self, value):
        stats, check_policy = get_password_strength(value)
        if stats.strength() < 0.60:
            raise BadRequest(
                f"Password is too weak! You need min {check_policy} "
                f"and strength above 0.6 current strength {stats.strength():.2f}"
            )

    @validates("email")
    def validate_email(self, value):
        exists = UserModel.query.filter_by(email=value).first()
        if exists:
            raise Conflict(f"The email you have entered is already registered!")

    @validates("phone")
    def validate_phone(self, value):
        exists = UserModel.query.filter_by(phone=value).first()
        if exists:
            raise Conflict(f"The phone you have entered is already registered!")


class UserLoginSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
