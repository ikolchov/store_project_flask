from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.purchase_product import PurchaseProductManager

# from schemas.request.user_product_interaction import ProductPurchaseSchema
from utils.decorators import user_required


class PurchaseProductResource(Resource):
    @auth.login_required
    @user_required()
    #  @validate_schema(ProductPurchaseSchema) needs fix
    def get(self):
        data = request.get_json()
        user = auth.current_user()
        saved, spend = PurchaseProductManager.get_product(data, user)
        return f"Order completed successfully total spend {spend:.2f} total saved {saved:.2f}"
