from flask import Flask
from config import Config
from flask_cors import CORS

from .authorization.routes import auth

from .models import db, login
from flask_migrate import Migrate

app = Flask(__name__)

cors = CORS(app, origins=['*'])

app.register_blueprint(auth)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

login.init_app(app)



from . import routes
from . import models
