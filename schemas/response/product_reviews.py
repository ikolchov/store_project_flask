from marshmallow import Schema, fields

from models import UserModel


class ProductReviewResponseSchema(Schema):
    review = fields.String()
    author = fields.Method("get_username")
    created_on = fields.Date()

    def get_username(self, obj):
        user = UserModel.query.filter_by(id=obj.author).first()

        return f"{user.first_name} {user.last_name}"

