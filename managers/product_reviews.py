from db import db
from managers.auth import auth
from models import ProductReviewsModel, ProductsModel


class ProductReviewManager:
    @staticmethod
    def add_review(data, id):
        data["item"] = id
        data["author"] = auth.current_user().id
        item = ProductsModel.query.filter_by(id=id).first()
        review = ProductReviewsModel(**data)
        item.reviews.append(review)
        db.session.flush()
        return review

    @staticmethod
    def get_top_comments(id, count):
        reviews = (
            ProductReviewsModel.query.filter_by(item=id)
            .order_by(ProductReviewsModel.rating.desc())
            .order_by(ProductReviewsModel.created_on.desc())
            .limit(count)
            .all()
        )
        return reviews
