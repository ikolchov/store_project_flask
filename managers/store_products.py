from flask import jsonify

from db import db
from models import ProductsModel, ProductStatus, EmployeeRoles
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
    def remove_product(product, employee):
        items = ProductsModel.query.filter_by(**product).all()
        if not items:
            raise ValueError("item does not exist")
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
