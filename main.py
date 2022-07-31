from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

app = Flask(__name__)
db.init_app(app)
api = Api(app)
migrate = Migrate(app, db)
app.config.from_object(config("config_credentials"))

[api.add_resource(*route_date) for route_date in routes]

@app.after_request
def return_response(resp):
    db.session.commit()
    return resp

if __name__ == "__main__":
    app.run()