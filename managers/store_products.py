from flask import jsonify

from db import db
from models import ProductsModel, ProductStatus
from utils.func_helpers import get_new_values


class StoreProductManager:

    @staticmethod
    def create_product(product):

        data = ProductsModel(**product)
        db.session.add(data)
        db.session.commit()
        return "item created successfully", 201

    @staticmethod
    def get_product(product):
        return ProductsModel.query.filter_by(**product).all()

    @staticmethod
    def update(product):
        new_value = product.pop("new_value")
        items = ProductsModel.query.filter_by(**product).all()
        changed = get_new_values(items, new_value)
        return "asd"

    @staticmethod
    def remove_product(product):
        items = ProductsModel.query.filter_by(**product).all()
        if not items:
            raise ValueError("item does not exist")
        for item in items:

            item.status = ProductStatus.delete
        db.session.commit()
        return items
