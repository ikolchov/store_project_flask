from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import ProductGroups, ProductsModel


class ProductDeleteResponseSchema(Schema):
    brand = fields.String()
    model = fields.String()
    description = fields.String()
    sku = fields.String()
    status = EnumField(ProductGroups)


class ProductReturnResponseSchema(ProductDeleteResponseSchema):
    status = EnumField(ProductGroups)


class ProductDiscountResponseSchema(Schema):
    item = fields.Method("get_item_info")
    discount = fields.Float()
    discount_start_date = fields.Date()
    discount_end_date = fields.Date()

    @staticmethod
    def get_item_info(obj):
        item = ProductsModel.query.filter_by(id=obj.item_id).first()
        return f"Brand: {item.brand} Model: {item.model} Price: {item.price:.2f} BGN"
