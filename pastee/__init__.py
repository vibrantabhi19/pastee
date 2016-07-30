from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter


app = Flask(__name__, static_folder='static/public')

app.config.from_pyfile('../config/config.cfg')
app.secret_key = 'fuckyoufuckingformsihopeyoudieinafire'

db = SQLAlchemy(app)


from pastee.routes import index
from pastee.routes import pastes
from pastee.routes import admin

from pastee.models import language
from pastee.models import paste
from pastee.models import user

db_adapter = SQLAlchemyAdapter(db, user.User)  # Register the User model
user_manager = UserManager(db_adapter, app)  # Initialize Flask-User
