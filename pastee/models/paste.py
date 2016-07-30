from pastee import db


class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paste_name = db.Column(db.Text)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    language = db.relationship('Language')
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, paste_name=None, language=None):
        self.paste_name = paste_name
        self.language = language
