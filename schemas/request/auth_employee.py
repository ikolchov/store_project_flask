
from marshmallow import Schema, fields
from marshmallow.validate import Length
from marshmallow_enum import EnumField

from models import ProductGroups


class EmployeeRegisterSchema(Schema):
    username = fields.String(requirerd=True)
    first_name = fields.String(required=True)
    mid_name = fields.String(required=True)
    last_name = fields.String(required=True)
    user_groups = EnumField(ProductGroups, by_value=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True, validate=Length(10))


class EmployeeLoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class EmployeeGroups(Schema):
    username = fields.String(required=True)
    user_groups = fields.String(required=True)

