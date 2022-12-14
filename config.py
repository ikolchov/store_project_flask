from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from mail import mail
from resources.routes import routes


#
# class ProductionConfig:
#     FLASK_ENV = "production"
#     DEBUG = False
#     TESTING = False
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
#         f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
#     )


class DevelopmentConfig:
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
    )
    MAIL_SERVER = f"{config('MAIL_SERVER')}"
    MAIL_PORT = 2525
    MAIL_USERNAME = f"{config('MAIL_USERNAME')}"
    MAIL_PASSWORD = f"{config('MAIL_PASSWORD')}"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class TestConfig:
    FLASK_ENV = "TEST"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('TEST_DB_USER')}:{config('TEST_DB_PASSWORD')}"
        f"@localhost:{config('TEST_DB_PORT')}/{config('TEST_DB_NAME')}"
    )
    MAIL_SERVER = f"{config('MAIL_SERVER')}"
    MAIL_PORT = 2525
    MAIL_USERNAME = f"{config('MAIL_USERNAME')}"
    MAIL_PASSWORD = f"{config('MAIL_PASSWORD')}"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


def create_app(config="config.DevelopmentConfig"):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(config)
    mail.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)
    api = Api(app)
    [api.add_resource(*route_data) for route_data in routes]
    mail.init_app(app)

    return app
