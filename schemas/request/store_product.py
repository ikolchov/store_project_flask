from marshmallow import Schema, fields, validates, validate
from marshmallow_enum import EnumField

from models import ProductGroups, ProductStatus


class ProductCreateSchema(Schema):

    product_group = EnumField(ProductGroups, by_value=True)
    brand = fields.String(required=True, validate=validate.Length(min=1, max=20))
    model = fields.String(required=True, validate=validate.Length(min=1, max = 100))
    description = fields.String(required=True)
    sku = fields.String(required=True)
    status = EnumField(ProductStatus, by_value=True)



