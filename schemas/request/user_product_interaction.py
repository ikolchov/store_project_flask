from marshmallow import Schema, fields, validates
from werkzeug.exceptions import BadRequest, NotFound

from models import ProductsModel, ProductStatus


class ProductReviewSchema(Schema):
    review = fields.String(required=True)


class ProductReviewResultsSchema(Schema):
    top = fields.Integer(required=True)


class SingleItemPurchase(Schema):
    product_id = fields.Integer()
    qty = fields.Integer()

    @validates("qty")
    def validate_purchase(self, value):
        if value <= 0:
            raise BadRequest("Invalid order")

    @validates("product_id")
    def validate_product(self, value):
        item = ProductsModel.query.filter_by(id=value).first()
        if not item.status == ProductStatus.active:
            raise NotFound("item not found!")
        if not item:
            raise BadRequest("invalid order")


# class ProductPurchaseSchema(Schema):
#     data = fields.List(fields.Nested(SingleItemPurchase), many=True)
