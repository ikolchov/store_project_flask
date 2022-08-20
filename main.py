

from config import create_app
from db import db

app = create_app()
print(app.config)


@app.after_request
def return_response(resp):
    db.session.commit()
    return resp


if __name__ == "__main__":
    app.run()