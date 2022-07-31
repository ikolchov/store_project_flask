from db import db
from sqlalchemy import func


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(14), nullable=False)
    last_name = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())


user_product = db.Table(
    "user_products",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"))
)
