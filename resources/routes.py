from resources.auth_employee import EmployeeRegisterResource, EmployeeLoginResource
from resources.auth_user import RegisterResource, LoginResource
from resources.change_password import ChangePasswordResource
from resources.product_reviews import ProductReviewResource
from resources.store_products import StoreProductResource
#from resources.tester import SendMail

routes = (
    (RegisterResource, '/register/'),
    (LoginResource, '/login/'),
    (EmployeeRegisterResource, '/administration/'),
    (EmployeeLoginResource, '/employee_login/'),
    (ChangePasswordResource, '/change_password/'),
    (StoreProductResource, '/store_data_platform/'),
    (ProductReviewResource, '/product_review/<int:id>')
    #exporter
   # (SendMail, '/mail/')


)