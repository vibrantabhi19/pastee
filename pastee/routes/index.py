from flask import render_template
from pastee import app
from pastee.models.user import User
from flask_user import current_user


@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)
