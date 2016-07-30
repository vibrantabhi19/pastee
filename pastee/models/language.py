from pastee import db


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    identifier = db.Column(db.Text)

    def __init__(self, name):
        self.name = name
