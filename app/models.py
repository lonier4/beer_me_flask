from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=True, default='')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email.lower()
        self.password = generate_password_hash(password)
        self.id = str(uuid.uuid4())

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'date_created': self.date_created
    }