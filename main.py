from decouple import config
from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api

from config import create_app
from db import db
from mail import mail

from resources.routes import routes

app = create_app()


@app.after_request
def return_response(resp):
    db.session.commit()
    return resp


if __name__ == "__main__":
    app.run()