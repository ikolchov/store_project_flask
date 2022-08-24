from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.export_data import ExportDataManager
from models import EmployeeRoles
from utils.decorators import validate_schema, permission_required


class ExportDataResource(Resource):
    @auth.login_required
#    @validate_schema(needs creation)
    @permission_required([EmployeeRoles.owner])
    def get(self):
        data = request.get_json()
        resp= ExportDataManager.get_report(data)