from marshmallow import Schema, fields, validates


class ChangePasswordSchema(Schema):
    username = fields.String(required=True)
    old_password = fields.String(required=True)
    new_password = fields.String(required=True)
    confirm_new_password = fields.String(required=True)



class ResetPasswordSchema(Schema):
    username = fields.String(required=True)

