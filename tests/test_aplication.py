from flask_testing import TestCase

from config import create_app
from db import db
from models import EmployeeRoles
from tests.factories import UserModelFactory, EmployeeModelFactory
from tests.test_func_helpers import generate_token

ENDPOINTS_DATA = {
    # '/register/': ['post'], - no login req
    # '/login/': ['post'], - no login req
    "/administration/": ["post", "put"],
    # '/employee_login/': ['post'], - no login req
    # '/change_password/': ['put', 'get'], - no login req
    "/store_data_platform/": ["put", "get", "delete", "patch"],
    "/product_review/1/": ["put", "get"],
    "/administration/price/": ["put", "get"],
    "/purchase_products/": ["get"],
    "/administration/report/": ["get"],
}

EMPLOYEE_ENDPOINTS_DATA = {
    "/administration/": ["post", "put"],
    "/store_data_platform/": ["put", "get", "delete", "patch"],
    "/administration/price/": ["put", "get"],
    "/administration/report/": ["get"],
}

USER_ENDPOINTS_DATA = {
    "/product_review/1/": ["put", "get"],
    "/purchase_products/": ["get"],
}


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def iterate_endpoints(self, data, status_code_method, exp_resp, headers=None):
        if not headers:
            headers = {}
        resp = None
        for end_point, action in data.items():
            for a in action:
                resp = eval(f"self.client.{a}('{end_point}', headers={headers})")
                status_code_method(resp)
                self.assertEqual(resp.json, exp_resp)

    def test_login_required(self):
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Missing token"}
        )

    def test_invalid_token(self):
        headers = {"Authorization": "Bearer eyJ0eX"}
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Invalid token"}, headers
        )

    def test_user_logging_in_admin_part(self):
        user = UserModelFactory()

        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        self.iterate_endpoints(
            EMPLOYEE_ENDPOINTS_DATA,
            self.assert_403,
            {"message": "You are a customer this is not available for you!"},
            headers,
        )

    def test_employee_logging_in_user_part(self):
        employee = EmployeeModelFactory()
        token = generate_token(employee)
        headers = {"Authorization": f"Bearer {token}"}
        self.iterate_endpoints(
            USER_ENDPOINTS_DATA,
            self.assert_403,
            {"message": "You are employee this is not available for you!"},
            headers,
        )

    def test_only_owner_can_get_reports(self):

        employee = EmployeeModelFactory()
        roles = [EmployeeRoles.senior, EmployeeRoles.worker, EmployeeRoles.manager]
        for role in roles:
            employee.user_role = role
            token = generate_token(employee)
            headers = {"Authorization": f"Bearer {token}"}
            resp = self.client.get("/administration/report/", headers=headers)
            self.assert_403(resp)
