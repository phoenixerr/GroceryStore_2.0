from flask import Flask
from application.config import Config, SECRET_KEY
from passlib.hash import pbkdf2_sha256 as passhash
from application.database import db
from application.models import *
from flask_cors import CORS


app=None

def create_app():
    app=Flask(__name__)
    # CORS(app)
    CORS(app, origins='http://localhost:5173')
    app.config.from_object(Config)
    app.secret_key=SECRET_KEY
    db.init_app(app)
    app.app_context().push()
    
    # db.create_all()

    # app.app_context().push()
    return app

app = create_app()

from application.apis import *

if __name__=="__main__":
    app.run(host='0.0.0.0', port=1430)