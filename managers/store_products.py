from db import db
from models import ProductsModel


class StoreProductManager:

    @staticmethod
    def create_product(product):
        product["modified_by"] = 1
        data = ProductsModel(**product)
        db.session.add(data)
        db.session.commit()
        return "item created successfully", 201

    @staticmethod
    def get_product(product):
        pass

    @staticmethod
    def update(product):
        pass

    @staticmethod
    def remove_product(product):
        pass
