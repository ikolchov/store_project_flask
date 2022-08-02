from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from managers.employees import EmployeeManager

from schemas.request.auth_employee import EmployeeSignInSchema
from utils.decorators import validate_schema


class EmployeeRegisterResource(Resource):

    @validate_schema(EmployeeSignInSchema)
    def post(self):
        employee_data = request.get_json()
        resp = EmployeeManager.register(employee_data)
        return resp # change this




