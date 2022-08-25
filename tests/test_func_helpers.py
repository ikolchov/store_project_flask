from managers.auth import AuthManager


def generate_token(user):
    token = AuthManager.encode_token(user)
    return token


def mock_secrets():
    return "111111111111111111"
