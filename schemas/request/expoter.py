from marshmallow import Schema, fields, validates_schema
from werkzeug.exceptions import BadRequest


class ExportDateValidationSchema(Schema):

    start_date = fields.Date()
    end_date = fields.Date()

    @validates_schema
    def validate_start_end(self, data, **kwargs):
        if data["start_date"] >= data["end_date"]:
            raise BadRequest("check start-end date")
