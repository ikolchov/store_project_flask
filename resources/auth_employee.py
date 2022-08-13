from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.employees import EmployeeManager
from models import EmployeeRoles

from schemas.request.auth_employee import EmployeeRegisterSchema, EmployeeLoginSchema, EmployeeGroups
from utils.decorators import validate_schema, permission_required


class EmployeeRegisterResource(Resource):

    @auth.login_required
    @permission_required(EmployeeRoles.manager)
    @validate_schema(EmployeeRegisterSchema)
    def post(self):
        employee_data = request.get_json()
        resp = EmployeeManager.register(employee_data)
        return resp

    @auth.login_required
    @permission_required(EmployeeRoles.manager)
    @validate_schema(EmployeeGroups)
    def put(self):
        data = request.get_json()

        resp = EmployeeManager.update_user_groups(data)
        return resp


class EmployeeLoginResource(Resource):
    @validate_schema(EmployeeLoginSchema)
    def post(self):
        data = request.get_json()
        token = EmployeeManager.login(data)
        return {"token": token}, 201
