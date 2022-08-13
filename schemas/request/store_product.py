from marshmallow import Schema, fields, validates, validate
from marshmallow_enum import EnumField

from models import ProductGroups, ProductStatus


class ProductCreateSchema(Schema):
    product_group = EnumField(ProductGroups)
    brand = fields.String(required=True, validate=validate.Length(min=1, max=20))
    model = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True)
    sku = fields.String(required=True)


class ProductGetSchema(Schema):
    product_group = EnumField(ProductGroups)
    brand = fields.String(validate=validate.Length(min=1, max=20))
    model = fields.String(validate=validate.Length(min=1, max=100))
    sku = fields.String()
    status = EnumField(ProductStatus, default=ProductStatus.active)


class ProductDeleteSchema(Schema):
    product_group = EnumField(ProductGroups)
    brand = fields.String(required=True, validate=validate.Length(min=1, max=20))
    model = fields.String(required=True, validate=validate.Length(min=1, max=100))
    sku = fields.String(required=True)


class ProductUpdateSchema(Schema):
    product_group = EnumField(ProductGroups)
    brand = fields.String(rvalidate=validate.Length(min=1, max=20))
    model = fields.String(validate=validate.Length(min=1, max=100))
    new_value = fields.Dict(required=True)

    @validates("new_value")
    def validate_keys_to_modify(self, value):
        values_to_modify = ["brand", "model", "description", "sku", "review"]
        if not all(k in values_to_modify for k in value.keys()):
            raise ValueError("invalid values to modify")

