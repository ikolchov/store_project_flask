from password_strength import PasswordPolicy, PasswordStats

from models import EmployeeModel


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


