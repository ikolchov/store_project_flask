from flask import request
from flask_restful import Resource

from managers.store_products import StoreProductManager
from schemas.request.store_product import ProductCreateSchema
from utils.decorators import validate_schema


class StoreProductResource(Resource):

    @validate_schema(ProductCreateSchema)
    def put(self):
        data = request.get_json()
        resp = StoreProductManager.create_product(data)
        return resp

    def get(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass