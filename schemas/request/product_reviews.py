from marshmallow import Schema, fields


class ProductReviewSchema(Schema):
    review = fields.String(required=True)


class ProductReviewResults(Schema):
    top = fields.Integer(required=True)

