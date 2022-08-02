from db import db

from models.enums import EmployeeRoles, ProductGroup


class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), nullable=False, unique=True)
    first_name = db.Column(db.String(14), nullable=False)
    mid_name = db.Column(db.String(14), nullable=False)
    last_name = db.Column(db.String(14), nullable=False)
    user_role = db.Column(db.Enum(EmployeeRoles),  default=EmployeeRoles.worker)
    user_groups = db.Column(db.Enum(ProductGroup), default=None)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
