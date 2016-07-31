from wtforms import Form, TextAreaField, SelectField
from wtforms.validators import DataRequired

from pastee.util.util import pretty_output


class PasteForm(Form):
    paste_text = TextAreaField('Text', [DataRequired()])
    paste_language = SelectField('Paste Language', choices=pretty_output())
