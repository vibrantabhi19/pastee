from pastee import app
from flask import render_template, request, redirect, url_for, flash
from flask_user import current_user

import random
import string

from pastee.models.paste import Paste
from pastee.models.language import Language
from pastee.forms.forms import PasteForm
from pastee import db

from pastee.util.util import create_file, read_paste, delete_paste


@app.route('/paste/add', methods=['GET', 'POST'])
def add():
    form = PasteForm(request.form)

    if request.method == 'POST' and form.validate():
        rand_name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

        language = Language.query.filter(Language.identifier == form.paste_language.data).first()
        paste = Paste(paste_name=rand_name, language=language)

        if current_user.is_authenticated:
            current_user.pastes.append(paste)

        form.populate_obj(paste)
        db.session.add(paste)
        db.session.commit()

        create_file(rand_name, form.paste_text.data)

        return redirect(url_for('view', paste_name=rand_name))

    return render_template('paste/add.html', form=form)


@app.route('/paste/view/<paste_name>')
def view(paste_name):
    paste = Paste.query.filter(Paste.paste_name == paste_name).first_or_404()
    paste_content = read_paste(paste_name)

    return render_template('paste/view.html', paste=paste, paste_content=paste_content, current_user=current_user)


@app.route('/paste/delete/<paste_name>')
def delete(paste_name):
    if not delete_paste(paste_name):
        flash('Error deleting paste', 'danger')
    else:
        paste = Paste.query.filter(Paste.paste_name == paste_name).first()
        paste.is_deleted = True
        db.session.commit()

        flash('Paste deleted correctly', 'success')

    return redirect('dashboard' if current_user.is_authenticated else 'index')
