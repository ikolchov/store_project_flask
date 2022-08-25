from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from db import db
from managers.auth import AuthManager
from models import EmployeeModel, GroupModel, EmployeeProductGroups
from utils.func_helpers import get_user_name, get_password, send_mail_credentials


class EmployeeManager:
    @staticmethod
    def register(employee_data):
        employee_data["password"], generated_password = get_password()
        employee_data["username"] = get_user_name(
            employee_data["first_name"], employee_data["last_name"]
        )
        employee = EmployeeModel(**employee_data)
        body = (
            f"Your username is {employee.username} \n"
            f"Your current password is- {generated_password}. Please login and change it!"
        )
        send_mail_credentials(
            employee, generated_password, "Your user has been created", body
        )

        db.session.add(employee)
        db.session.commit()
        return f"User created successfully", 201

    @staticmethod
    def login(employee_data):
        employee = EmployeeModel.query.filter_by(
            username=employee_data["username"]
        ).first()
        if not employee:
            raise BadRequest("You are not logged in!")
        if check_password_hash(employee.password, employee_data["password"]):
            return AuthManager.encode_token(employee)
        raise BadRequest("Wrong Password!")

    @staticmethod
    def update_user_groups(data):
        employee = EmployeeModel.query.filter_by(username=data["username"]).first()
        # check for employee first to avoid 1 more search in db
        if not employee:
            raise BadRequest("Invalid username!")
        pgs = GroupModel.query.filter_by(groups=data["user_groups"]).first()
        data["user_groups"] = pgs.id
        emp_pgs = EmployeeProductGroups(**data)
        db.session.add(emp_pgs)
        db.session.commit()
        return f"PG {pgs.groups} successfully added for user {employee.username}"
