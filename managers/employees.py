import secrets

from werkzeug.security import generate_password_hash

from db import db
from models import EmployeeModel
from utils.func_helpers import get_user_name


class EmployeeManager:
    @staticmethod
    def register(employee_data):
        employee_data["password"] = secrets.token_urlsafe(10)
        employee_data["username"] = get_user_name(employee_data["first_name"], employee_data["last_name"])
        employee = EmployeeModel(**employee_data)
        db.session.add(employee)
        db.session.commit()
        return "asd"
