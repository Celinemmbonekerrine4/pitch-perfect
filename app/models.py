from . import login_manager
from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash

class Pitch(db.Model):

   __tablename__ = 'pitches'
   id = db.Column(db.Integer,primary_key = True)

   name = db.Column(db.String(255))
   users = db.relationship('User', backref = 'pitch', lazy='dynamic')

   def  __init__(self,id,title,pitch,vote_average,vote_count):
    self.id = id
    self.title = title
    self.pitch = pitch
    self.vote_average = vote_average
    self.vote_count = vote_count

    all_pitches = []

    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
      Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls):

      response = []

      for pitch in cls.all_pitches:
        if pitch.pitch_id == id:
          response.append(pitch)

        return response


    
      def __repr__(self):
        return f'User{self.name}'



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
  







  


    
    