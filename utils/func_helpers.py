from password_strength import PasswordPolicy, PasswordStats
from werkzeug.exceptions import Forbidden

from models import EmployeeModel, EmployeeProductGroups, GroupModel


def get_password_strength(value):
    policy = PasswordPolicy.from_names(
        length=8,  # min length: 8
        uppercase=1,  # need min. 1 uppercase letters
        numbers=2,  # need min. 2 digits
        special=1,  # need min. 1 special characters
        nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
    )
    stats = PasswordStats(value)
    check_policy = policy.test(value)
    return stats, check_policy


def get_user_name(first, last):
    user_name = f"{first[:3]}{last[:3]}"
    counter = 1
    while True:
        user_exists = EmployeeModel.query.filter_by(username=user_name).first()
        if user_exists:
            user_name = f"{first[:3]}{last[:3]}{counter}"
            counter += 1
        elif not user_exists:
            break
    return user_name


def get_new_values(items, new_value):

    for item in items:
        for k, v in new_value.items():
            setattr(item, k, v)


def check_permissions(pg, user):

    emp_pg = GroupModel.query.filter_by(groups=pg["product_group"]).first()
    perm = EmployeeProductGroups.query.filter_by(username=user.username, user_groups=emp_pg.id).first()
    if not perm:
        raise Forbidden("you don`t have permissions")
    return True
