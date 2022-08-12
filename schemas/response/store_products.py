from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import ProductGroups


class ProductReturnSchema(Schema):
    brand = fields.String()
    model = fields.String()
    description = fields.String()
    sku = fields.String()
    status = EnumField(ProductGroups)