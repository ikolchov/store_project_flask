import secrets

from marshmallow import Schema, fields
from marshmallow.validate import Length
from marshmallow_enum import EnumField

from models import ProductGroup


class EmployeeSignInSchema(Schema):
    username = fields.String(requirerd=True)
    first_name = fields.String(required=True)
    mid_name = fields.String(required=True)
    last_name = fields.String(required=True)
    user_groups = EnumField(ProductGroup, by_value=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True, validate=Length(10))

