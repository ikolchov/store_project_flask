from db import db
from sqlalchemy import func

from models.enums import ProductGroups, ProductStatus

product_reviews_relation_table = db.Table(
    'product_reviews_relation_table',
    db.Column('item_id', db.Integer, db.ForeignKey("products.id")),
    db.Column('comment_id', db.Integer, db.ForeignKey('product_reviews.id'))
)


class ProductsModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_group = db.Column(db.Enum(ProductGroups), nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    sku = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(ProductStatus), nullable=False, default=ProductStatus.active)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    modified_on = db.Column(db.DateTime, onupdate=func.now())
    modified_by = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    reviews = db.relationship("ProductReviewsModel", secondary=product_reviews_relation_table)


class ProductDetailsModel(db.Model):
    __tablename__ = "product_details"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    discount = db.Column(db.Float, default=0)
    discount_start_date = db.Column(db.Date, server_default=func.now())
    discount_end_date = db.Column(db.Date, db.Constraint('discount_end_date'>discount_start_date))  # add some req


class ProductReviewsModel(db.Model):
    __tablename__ = "product_reviews"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=0)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
