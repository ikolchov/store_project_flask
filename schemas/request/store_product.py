from datetime import datetime

from marshmallow import Schema, fields, validates, validate, validates_schema
from marshmallow_enum import EnumField
from werkzeug.exceptions import BadRequest

from models import ProductGroups, ProductStatus, ProductsModel


class ProductCreateSchema(Schema):
    product_group = EnumField(ProductGroups)
    brand = fields.String(required=True, validate=validate.Length(min=1, max=20))
    model = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True)
    sku = fields.Integer(required=True)
    price = fields.Float(required=True)

    @validates("sku")
    def validate_item_does_not_exist(self, value):
        item = ProductsModel.query.filter_by(sku=value).first()
        if item:
            raise BadRequest("Item already exists!")


class ProductGetSchema(Schema):
    product_group = EnumField(ProductGroups)
    brand = fields.String(validate=validate.Length(min=1, max=20))
    model = fields.String(validate=validate.Length(min=1, max=100))
    sku = fields.Integer()
    status = EnumField(ProductStatus, default=ProductStatus.active)


class ProductDeleteSchema(Schema):
    product_group = EnumField(ProductGroups)
    brand = fields.String(required=True, validate=validate.Length(min=1, max=20))
    model = fields.String(required=True, validate=validate.Length(min=1, max=100))
    sku = fields.Integer(required=True)


class ProductUpdateSchema(Schema):

    product_group = EnumField(ProductGroups, required=True)
    brand = fields.String(required=True)
    model = fields.String(required=True)
    new_value = fields.Dict(required=True)

    # new_value = dict with optional values to modify
    @validates("new_value")
    def validate_keys_to_modify(self, value):
        values_to_modify = ["brand", "model", "description", "sku", "price"]
        if not all(k in values_to_modify for k in value.keys()):
            raise ValueError("invalid values to modify")


class ProductPriceSchema(Schema):
    item_id = fields.Integer(required=True)
    discount = fields.Float()
    discount_start_date = fields.Date()
    discount_end_date = fields.Date()

    @validates_schema
    def validate_start_end(self, data, **kwargs):
        if data["discount_start_date"] >= data["discount_end_date"]:
            raise BadRequest("check start-end date")

    @validates("item_id")
    def validates_item_is_active(self, value):
        item = ProductsModel.query.filter_by(id=value).first()
        if not item:
            raise BadRequest("item does not exist!")
        if not item.status == ProductStatus.active:
            raise BadRequest("item is not active please check again!")

    @validates("discount")
    def validate_discount(self, value):
        if not 0 <= value < 100:
            raise BadRequest("discount needs to be between 0% and 100%")

    @validates("discount_end_date")
    def validate_discount_end_date(self, value):
        cur_date = datetime.now().date()
        if value < cur_date:
            raise BadRequest(f"invalid time stamp current date is {cur_date}")
