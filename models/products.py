from db import db
from sqlalchemy import func

from models.enums import ProductGroup, ProductStatus


class ProductsModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_group = db.Column(db.Enum(ProductGroup), nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sku = db.Column(db.Integer, db.ForeignKey("product_details.id"), nullable=False)  # try change
    review = db.Column(db.Integer, db.ForeignKey("product_reviews.id"))
    status = db.Column(db.Enum(ProductStatus), nullable=False, default=ProductStatus.active)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    modified_on = db.Column(db.DateTime, nullable=False, onupdate=func.now())
    modified_by = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)


class ProductDetailsModel(db.Model):
    __tablename__ = "product_details"

    id = db.Column(db.Integer, primary_key=True) #change id with sku?

    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    discount_end_date = db.Column(db.DateTime, nullable=False)  # add some req


class ProductReviews(db.Model):
    __tablename__ = "product_reviews"

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=0)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)




