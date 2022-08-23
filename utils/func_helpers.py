import datetime
import secrets
import uuid

from decouple import config
from flask_mail import Message
from password_strength import PasswordPolicy, PasswordStats
from werkzeug.exceptions import Forbidden, NotFound
from werkzeug.security import generate_password_hash

from mail import mail
from models import EmployeeModel, EmployeeProductGroups, GroupModel, UserModel


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


def get_password():
    generated_password = secrets.token_urlsafe(12)
    hash_password = generate_password_hash(generated_password)
    return hash_password, generated_password


def send_mail_credentials(user, pw):
    msg = Message("Your user has been created", sender=f"{config('MAIL_USERNAME')}", recipients=[f"{user.email}"])
    msg.body = f"Your username is {user.username}" \
               f"Your current password is- {pw}. Please login and change it!"
    mail.send(msg)
    a = 5


def get_user(data):
    if "@" in data["username"]:
        user = UserModel.query.filter_by(email=data["username"]).first()
    else:
        user = EmployeeModel.query.filter_by(username=data["username"]).first()
    if not user:
        raise NotFound("Username not found!")
    return user


def get_filename_generator(data):

    for k, v in data.items():
        data[k] = datetime.datetime.strptime(v, '%Y-%m-%d').strftime('%Y%m%d')
    data['unique_ext'] = uuid.uuid4()

    file_name = f"{data['start_date']}_{data['end_date']}_{data['unique_ext']}.xlsx"
    temp_dir = r'.\service_dropbox\temp_file_dir' + file_name
    return file_name, temp_dir


