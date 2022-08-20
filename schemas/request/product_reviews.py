from marshmallow import Schema, fields


class ProductReviewSchema(Schema):
    review = fields.String(required=True)

