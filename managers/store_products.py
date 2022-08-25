from datetime import datetime

from werkzeug.exceptions import BadRequest

from db import db
from models import ProductsModel, ProductStatus, EmployeeRoles, ProductDetailsModel
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
        if not items:
            raise BadRequest("There are no items with this search condition")
        old, new = get_new_values(items, new_value)
        return old, new

    @staticmethod
    def remove_product(product, employee):
        items = ProductsModel.query.filter_by(**product).all()
        if not items:
            raise BadRequest("item does not exist")
        # soft delete by regular employee
        if employee.user_role in [EmployeeRoles.worker, EmployeeRoles.senior]:
            for item in items:
                item.status = ProductStatus.delete
                item.modified_by = employee.id
        # hard delete for users with more rights
        elif employee.user_role in [EmployeeRoles.manager, EmployeeRoles.owner]:
            for item in items:
                db.session.delete(item)
        db.session.commit()
        return items


class ProductPriceManager:
    @staticmethod
    def create_discount(item):
        data = ProductDetailsModel(**item)
        db.session.add(data)
        db.session.commit()
        return data

    @staticmethod
    def get_discounts():
        date = datetime.now().date()
        discount_items = ProductDetailsModel.query.filter(
            ProductDetailsModel.discount_end_date > date
        ).all()
        return discount_items
