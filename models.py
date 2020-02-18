from . import db

from werkzeug.security import generate_password_hash,check_password_hash

class User:
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))



def __repr__(self):
    return f'User{self.username}'

