from resources.auth_employee import EmployeeRegisterResource, EmployeeLoginResource
from resources.auth_user import RegisterResource, LoginResource
from resources.store_products import StoreProductResource

routes = (
    (RegisterResource, '/register/'),
    (LoginResource, '/login/'),
    (EmployeeRegisterResource, '/administration/'),
    (EmployeeLoginResource, '/employee_login/'),
    #add change pass
    (StoreProductResource, '/store_data_platform/')

)