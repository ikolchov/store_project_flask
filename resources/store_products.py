from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.store_products import StoreProductManager
from models import ProductStatus
from schemas.request.store_product import ProductCreateSchema, ProductGetSchema, ProductUpdateSchema, \
    ProductDeleteSchema
from schemas.response.store_products import ProductReturnResponseSchema, ProductDeleteResponseSchema
from utils.decorators import validate_schema
from utils.func_helpers import check_permissions


class StoreProductResource(Resource):
    @auth.login_required
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
    @validate_schema(ProductGetSchema)
    def get(self):
        data = request.get_json()
        if "status" not in data.keys():
            data["status"] = "active"
        items = StoreProductManager.get_product(data)
        return ProductReturnResponseSchema().dump(items, many=True), 201

    @auth.login_required
    @validate_schema(ProductDeleteSchema)
    def delete(self):
        data = request.get_json()
        data["status"] = "active"
        items = StoreProductManager.remove_product(data)
        return ProductDeleteResponseSchema().dump(items, many=True), 201

    @auth.login_required
    @validate_schema(ProductUpdateSchema)
    def patch(self):
        data = request.get_json()
        StoreProductManager.update(data)
        return "successfully modified", 201

