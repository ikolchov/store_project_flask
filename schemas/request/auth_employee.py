from marshmallow import Schema, fields, validates, validates_schema
from marshmallow_enum import EnumField
from werkzeug.exceptions import Conflict, BadRequest

from models import ProductGroups, EmployeeModel, EmployeeProductGroups, GroupModel


class EmployeeRegisterSchema(Schema):

    first_name = fields.String(required=True)
    mid_name = fields.String(required=True)
    last_name = fields.String(required=True)
    user_groups = EnumField(ProductGroups, by_value=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)

    @validates("email")
    def validate_email(self, value):
        exists = EmployeeModel.query.filter_by(email=value).first()
        if exists:
            raise Conflict(
                f"The email is already registered, please contact the admins for further checks!"
            )

    @validates("phone")
    def validate_phone(self, value):
        if len(value) != 10:
            raise BadRequest(f"Invalid phone number!")
        exists = EmployeeModel.query.filter_by(phone=value).first()
        if exists:
            raise Conflict(
                f"The phone is already registered, please contact the admins for further checks!"
            )


class EmployeeGroups(Schema):
    username = fields.String(required=True)
    user_groups = EnumField(ProductGroups)

    @validates_schema
    def validate_employee_has_no_rights(self, data, **kwargs):
        employee_pgs = EmployeeProductGroups.query.filter_by(
            username=data["username"]
        ).all()
        group_id = GroupModel.query.filter_by(groups=data["user_groups"]).first()
        for employee_pg in employee_pgs:
            if group_id.id == employee_pg.user_groups:
                raise BadRequest("User is already authorised")


class EmployeeLoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
