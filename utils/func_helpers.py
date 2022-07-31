from password_strength import PasswordPolicy, PasswordStats


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