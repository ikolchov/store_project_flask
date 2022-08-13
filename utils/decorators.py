from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth
from models import EmployeeProductGroups


def validate_schema(schema_name):
    def decorated_func(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if not errors:
                return func(*args, **kwargs)
            raise BadRequest(errors)

        return wrapper

    return decorated_func


def permission_required(role):
    def decorated_func(func):
        def wrapper(*args, **kwargs):
            current_user = auth.current_user()
            if not current_user.user_role == role:
                raise Forbidden("you don`t have permissions")  # fix
            return func(*args, **kwargs)

        return wrapper

    return decorated_func



