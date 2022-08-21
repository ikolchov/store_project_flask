from datetime import datetime

from db import db
from managers.auth import auth
from models import ProductsModel, ProductDetailsModel, UserProductsLogger


class PurchaseProductManager:

    @staticmethod
    def get_product(items, user):
        cur_time = datetime.now().date()
        total_amount = 0
        total_saved = 0
        #add funcs
        for item_purchased in items:
            item_id = item_purchased['product_id']
            item = ProductsModel.query.filter_by(id=item_id).first()
            get_discount = ProductDetailsModel.query.filter_by(item_id=item_id).filter(
                ProductDetailsModel.discount_end_date >= cur_time).first()
            discount = 0 if not get_discount else get_discount.discount
            calc_discount = round((discount * item.price/100), 2)
            total_amount += (item.price - calc_discount) * item_purchased["qty"]
            total_saved += calc_discount * item_purchased["qty"]
            logger = {
                'user_id': user.id,
                "item_id": item_id,
                "order_create_date": cur_time,
                "price": item.price,
                "qty": item_purchased["qty"],
                "discount": discount
            }
            data = UserProductsLogger(**logger)
            db.session.add(data)
        db.session.flush()


        return data



