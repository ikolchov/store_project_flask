import secrets

from decouple import config
from flask_mail import Message
from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash, generate_password_hash

from db import db
from mail import mail

from managers.auth import AuthManager
from models import EmployeeModel, GroupModel, EmployeeProductGroups

from utils.func_helpers import get_user_name


class EmployeeManager:

    @staticmethod
    def register(employee_data):
        generated_password = secrets.token_urlsafe(12)
        employee_data["password"] = generate_password_hash(generated_password)
        employee_data["username"] = get_user_name(employee_data["first_name"], employee_data["last_name"])
        employee = EmployeeModel(**employee_data)
        msg = Message("Your user has been created", sender=f"{config('MAIL_USERNAME')}", recipients=[f"{employee.email}"])
        msg.body = f"Your username is {employee_data['username']}" \
                   f"Your current password is- {generated_password}. Please login and change it!"
        mail.send(msg)
        db.session.add(employee)
        db.session.commit()
        return "User created successfully", 201

    @staticmethod
    def login(employee_data):
        employee = EmployeeModel.query.filter_by(username=employee_data["username"]).first()
        if not employee:
            raise BadRequest("You are not logged in!")
        if check_password_hash(employee.password, employee_data["password"]):
            return AuthManager.encode_token(employee)
        raise BadRequest("Wrong Password!")

    @staticmethod
    def update_user_groups(data):
        employee = EmployeeModel.query.filter_by(username=data["username"]).first()
        pgs = GroupModel.query.filter_by(groups=data['user_groups']).first()
        if not employee:
            raise BadRequest("Invalid username!")
        data["user_groups"] = pgs.id
        emp_pgs = EmployeeProductGroups(**data)
        db.session.add(emp_pgs)
        db.session.commit()
        return f"PG {pgs.groups} successfully added for user {employee.username}"
