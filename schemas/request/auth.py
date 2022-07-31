from marshmallow import Schema, fields, validates

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
        if stats.strength() < 0.01: #change this
            raise ValueError(f"Password is too weak! You need min {check_policy}")


class UserLoginSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
