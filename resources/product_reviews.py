from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.product_reviews import ProductReviewManager
from schemas.request.product_reviews import ProductReviewSchema, ProductReviewResults
from schemas.response.product_reviews import ProductReviewResponseSchema
from utils.decorators import validate_schema, user_required


class ProductReviewResource(Resource):

    @auth.login_required
    @user_required()
    @validate_schema(ProductReviewSchema)

    def put(self, id):
        data = request.get_json()
        review = ProductReviewManager.add_review(data, id)

        return ProductReviewResponseSchema().dump(review), 201

    @auth.login_required
    @user_required()
    @validate_schema(ProductReviewResults)

    def get(self, id):
        data = request.get_json()
        resp = ProductReviewManager.get_top_comments(id, data["top"])
        return ProductReviewResponseSchema().dump(resp, many=True)



