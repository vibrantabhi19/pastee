import os


def execfile(filename):
    globals = dict(__file__=filename)
    exec(open(filename).read(), globals)

activate_this = os.path.dirname(__file__) + '/venv/bin/activate_this.py'
execfile(activate_this)

import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, os.path.dirname(__file__))

from pastee import app as application