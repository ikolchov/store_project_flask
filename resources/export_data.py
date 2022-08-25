from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.export_data import ExportDataManager
from models import EmployeeRoles
from schemas.request.expoter import ExportDateValidationSchema
from utils.decorators import validate_schema, permission_required


class ExportDataResource(Resource):
    @auth.login_required
    @permission_required([EmployeeRoles.owner])
    @validate_schema(ExportDateValidationSchema)
    def get(self):
        data = request.get_json()
        resp = ExportDataManager.get_report(data)
        return resp
