from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.purchase_product import PurchaseProductManager
from utils.decorators import user_required


class PurchaseProductResource(Resource):

    @auth.login_required
    @user_required()
    def get(self):
        data = request.get_json()
        user = auth.current_user()
        resp = PurchaseProductManager.get_product(data, user)
        return resp