from resources.auth_employee import EmployeeRegisterResource
from resources.auth_user import RegisterResource, LoginResource

routes = (
    (RegisterResource, '/register/'),
    (LoginResource, '/login/'),
    (EmployeeRegisterResource, '/administration/'),
)