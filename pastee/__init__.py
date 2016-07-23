from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static/public')

app.config.from_pyfile('../config/config.cfg')
app.secret_key = 'fuckyoufuckingformsihopeyoudieinafire'

db = SQLAlchemy(app)


from pastee.routes import index
from pastee.routes import pastes

from pastee.models import language
from pastee.models import paste
