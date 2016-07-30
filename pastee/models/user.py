from pastee import db
from flask_user import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    email = db.Column(db.Text)
    pastes = db.relationship('Paste', backref='user', lazy='dynamic')
    is_enabled = True

    def __init__(self, username=None, password=None, is_active=None):
        self.username = username
        self.password = password
        self.active = is_active
        self.is_enabled = True
