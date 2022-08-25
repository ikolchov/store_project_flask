from marshmallow import Schema, fields


class ResetPasswordSchema(Schema):
    username = fields.String(required=True)


class ChangePasswordSchema(ResetPasswordSchema):

    old_password = fields.String(required=True)
    new_password = fields.String(required=True)
    confirm_new_password = fields.String(required=True)
