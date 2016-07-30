from pastee import app
from flask import render_template, request, redirect, url_for
from flask_user import current_user

import random
import string

from pastee.models.paste import Paste
from pastee.models.language import Language
from pastee.forms.forms import PasteForm
from pastee import db

from pastee.util.util import create_file, read_paste


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
    paste_content = read_paste(paste_name)
    paste = Paste.query.filter(Paste.paste_name == paste_name).first()

    return render_template('paste/view.html', paste=paste, paste_content=paste_content)
