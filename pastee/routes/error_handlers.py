from flask import render_template
from flask_user import current_user
from pastee import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', current_user=current_user), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html', current_user=current_user), 500
