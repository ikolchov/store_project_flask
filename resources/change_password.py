from flask import request
from flask_restful import Resource

from managers.change_password import PasswordManager
from schemas.request.change_password import ChangePasswordSchema, ResetPasswordSchema
from utils.decorators import validate_schema


class ChangePasswordResource(Resource):
    @validate_schema(ChangePasswordSchema)
    def put(self):
        data = request.get_json()
        return PasswordManager.change_password(data)

    @validate_schema(ResetPasswordSchema)
    def get(self):
        data = request.get_json()
        PasswordManager.reset_password(data)
        #TODO fix