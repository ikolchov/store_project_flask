from flask import request
from flask_restful import Resource

from managers.users import UserManager
from schemas.request.auth_user import UserSignInSchema, UserLoginSchema
from utils.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(UserSignInSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


class LoginResource(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}, 201
