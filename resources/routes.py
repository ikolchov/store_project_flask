from resources.auth_employee import EmployeeRegisterResource, EmployeeLoginResource
from resources.auth_user import RegisterResource, LoginResource
from resources.change_password import ChangePasswordResource
from resources.export_data import ExportDataResource

from resources.product_reviews import ProductReviewResource
from resources.purchase_product import PurchaseProductResource
from resources.store_products import StoreProductResource, StorePriceResource

# from resources.tester import SendMail

routes = (
    (RegisterResource, "/register/"),
    (LoginResource, "/login/"),
    (EmployeeRegisterResource, "/administration/"),
    (EmployeeLoginResource, "/employee_login/"),
    (ChangePasswordResource, "/change_password/"),
    (StoreProductResource, "/store_data_platform/"),
    (ProductReviewResource, "/product_review/<int:id>/"),
    (StorePriceResource, "/administration/price/"),
    (PurchaseProductResource, "/purchase_products/"),
    (ExportDataResource, "/administration/report/")
    # cart + main page
    # (SendMail, '/mail/')
)
