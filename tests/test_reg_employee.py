from flask_testing import TestCase

from config import create_app
from db import db
from models import EmployeeModel, EmployeeRoles
from tests.factories import EmployeeModelFactory
from tests.test_func_helpers import generate_token


class TestCreateEmployee(TestCase):
    URL = "/administration/"

    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_employee_missing_fields(self):
        employee = EmployeeModel.query.all()
        assert len(employee) == 0

        employee = EmployeeModelFactory()
        roles = [EmployeeRoles.manager, EmployeeRoles.owner]
        for role in roles:
            employee.user_role = role
            token = generate_token(employee)
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }

            data = {}
            resp = self.client.post(self.URL, headers=headers, json=data)
            self.assert_400(resp)
            info = ["Missing data for required field."]
            assert resp.json["message"] == {
                "phone": info,
                "email": info,
                "last_name": info,
                "first_name": info,
                "mid_name": info,
            }
        employee = EmployeeModel.query.all()
        assert len(employee) == 1

    def test_change_employee_groups(self):
        employee = EmployeeModel.query.all()
        assert len(employee) == 0

        employee = EmployeeModelFactory()
        roles = [EmployeeRoles.manager, EmployeeRoles.owner, EmployeeRoles.senior]
        for role in roles:
            employee.user_role = role
            token = generate_token(employee)
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }

            data = {}
            resp = self.client.put(self.URL, headers=headers, json=data)
            self.assert_400(resp)
            info = ["Missing data for required field."]
            assert resp.json["message"] == {"username": info}
        employee = EmployeeModel.query.all()
        assert len(employee) == 1
