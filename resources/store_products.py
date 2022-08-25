from flask import request
from flask_restful import Resource
from werkzeug.exceptions import NotFound

from managers.auth import auth
from managers.store_products import StoreProductManager, ProductPriceManager
from models import ProductStatus, EmployeeRoles
from schemas.request.store_product import (
    ProductCreateSchema,
    ProductGetSchema,
    ProductUpdateSchema,
    ProductDeleteSchema,
    ProductPriceSchema,
)
from schemas.response.store_products import (
    ProductReturnResponseSchema,
    ProductDeleteResponseSchema,
    ProductDiscountResponseSchema,
)
from utils.decorators import validate_schema, permission_required
from utils.func_helpers import check_permissions


class StoreProductResource(Resource):
    @auth.login_required
    @permission_required(
        [
            EmployeeRoles.manager,
            EmployeeRoles.owner,
            EmployeeRoles.senior,
            EmployeeRoles.worker,
        ]
    )
    @validate_schema(ProductCreateSchema)
    def put(self):
        data = request.get_json()
        employee = auth.current_user()
        check_permissions(data, employee)
        data["status"] = ProductStatus.active
        data["modified_by"] = employee.id
        resp = StoreProductManager.create_product(data)
        return resp, 201

    @auth.login_required
    @permission_required(
        [
            EmployeeRoles.manager,
            EmployeeRoles.owner,
            EmployeeRoles.senior,
            EmployeeRoles.worker,
        ]
    )
    @validate_schema(ProductGetSchema)
    def get(self):
        data = request.get_json()
        # if no status is provided by default will search in active ones only
        if "status" not in data.keys():
            data["status"] = "active"
        items = StoreProductManager.get_product(data)
        if not items:
            raise NotFound("No items found matching the criteria")
        return ProductReturnResponseSchema().dump(items, many=True), 201

    @auth.login_required
    @permission_required(
        [
            EmployeeRoles.manager,
            EmployeeRoles.owner,
            EmployeeRoles.senior,
            EmployeeRoles.worker,
        ]
    )
    @validate_schema(ProductDeleteSchema)
    def delete(self):
        data = request.get_json()
        employee = auth.current_user()
        check_permissions(data, employee)
        items = StoreProductManager.remove_product(data, employee)

        return ProductDeleteResponseSchema().dump(items, many=True), 201

    @auth.login_required
    @permission_required(
        [
            EmployeeRoles.manager,
            EmployeeRoles.owner,
            EmployeeRoles.senior,
            EmployeeRoles.worker,
        ]
    )
    @validate_schema(ProductUpdateSchema)
    def patch(self):
        data = request.get_json()
        employee = auth.current_user()
        check_permissions(data, employee)
        old, new = StoreProductManager.update(data)
        # needs fix
        resp = ""
        for k in old:
            resp += f"Old value of {k} was {old[k]}, new one is {new[k]} ."
        return resp


class StorePriceResource(Resource):
    @auth.login_required
    @permission_required(
        [EmployeeRoles.manager, EmployeeRoles.owner, EmployeeRoles.senior]
    )
    @validate_schema(ProductPriceSchema)
    def put(self):
        data = request.get_json()
        item = ProductPriceManager.create_discount(data)
        return ProductDiscountResponseSchema().dump(item)

    @auth.login_required
    @permission_required(
        [
            EmployeeRoles.manager,
            EmployeeRoles.owner,
            EmployeeRoles.senior,
            EmployeeRoles.worker,
        ]
    )
    def get(self):
        # current items on discount
        items = ProductPriceManager.get_discounts()
        return ProductDiscountResponseSchema().dump(items, many=True)
