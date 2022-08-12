from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.store_products import StoreProductManager
from models import ProductStatus
from schemas.request.store_product import ProductCreateSchema, ProductGetSchema
from schemas.response.store_products import ProductReturnSchema
from utils.decorators import validate_schema


class StoreProductResource(Resource):

    @validate_schema(ProductCreateSchema)
    def put(self):
        data = request.get_json()
        data["status"] = ProductStatus.active
        resp = StoreProductManager.create_product(data)
        return resp

    @validate_schema(ProductGetSchema)
    def get(self):
        data = request.get_json()
        if not data["status"]:
            data["status"] = "active"
        items = StoreProductManager.get_product(data)

        return ProductReturnSchema().dump(items, many=True), 201

    def delete(self):
        data = request.get_json()
        data["status"] = "active"
        item_id = StoreProductManager.remove_product(data)

        return f"item removed {item_id}", 201


    def patch(self):
        pass
