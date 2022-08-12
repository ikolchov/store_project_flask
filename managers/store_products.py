from db import db
from models import ProductsModel, ProductStatus


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
        return ProductsModel.query.filter_by(status=product["status"]).all()


    @staticmethod
    def update(product):
        pass

    @staticmethod
    def remove_product(product):
        item = ProductsModel.query.filter_by(**product).first()
        if not item:
            raise ValueError("item does not exist")
        item.status = ProductStatus.delete
        db.session.commit()
        return item.id
