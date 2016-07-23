from pastee.models.language import Language
from pastee.models.paste import Paste

import os

from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters import get_formatter_by_name

from pygments.util import ClassNotFound

PASTES_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/data/pastes/'


def read_paste(paste_name):
    paste = Paste.query.filter(Paste.paste_name == paste_name).first()
    paste_language = Language.query.filter(Language.identifier == paste.language.identifier).first()

    paste_content = read_file(paste_name)

    try:
        lexer = guess_lexer(paste_content)
    except ClassNotFound:
        lexer = get_lexer_by_name(paste_language.identifier)

    formatter = get_formatter_by_name('html')

    return highlight(paste_content, lexer, formatter)


def pretty_output():
    available_languages = Language.query.all()
    return_value = []

    for language in available_languages:
        return_value.append(tuple([language.identifier, language.name]))

    return list(return_value)


def create_file(file_name, file_content):
    file = PASTES_FOLDER + file_name
    with open(file, 'w') as f:
        f.write(file_content)


def read_file(file_name):
    file = PASTES_FOLDER + file_name
    with open(file, 'r') as f:
        contents = f.read()

    return contents
