from flask import request
from flask_restful import Resource

from managers.export_data import ExportDataManager


class ExportDataResource(Resource):

    def get(self):
        data = request.get_json()
        resp= ExportDataManager.get_report(data)