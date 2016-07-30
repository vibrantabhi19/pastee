from flask import render_template
from flask_user import login_required, current_user
from pastee import app
from pastee.models.paste import Paste


@app.route('/dashboard')
@login_required
def dashboard():
    own_pastes = Paste.query.filter(Paste.user_id == current_user.id).all()

    return render_template('dashboard/index.html', current_user=current_user, pastes=own_pastes)
