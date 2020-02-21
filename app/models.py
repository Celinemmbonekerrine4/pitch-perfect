from . import login_manager
from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class Pitch(db.Model):

  __tablename__ = 'pitches'
  id = db.Column(db.Integer,primary_key = True)
  pitch_id = db.Column(db.Integer)
  pitch_title = db.Column(db.String)
  image_path = db.Column(db.String)
  pitch_review = db.Column(db.String)
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

  def save_pitch(self):
      db.session.add(self)
      db.session.commit()

  @classmethod
  def get_pitch(cls,id):
      pitch = Pitch.query.filter_by(pitch_id=id).all()
      return pitch


  
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



class Interview:

  all_interviews = []

  def __init__(self,title,pitch):
    self.title = title
    self.pitch = pitch

  def save_interview(self):
      Interview.all_interview.append(self)


class BusinessPlan:

  all_businessplans = []
  
  def __init__(self,title,pitch):
    self.title = title
    self.pitch = pitch

  def save_businessplan(self):
      BusinessPlan.all_businessplans.append(self)
 

class Life:

  all_life = []

def __init__(self,title,pitch):
  self.title = title
  self.pitch = pitch

def save_life(self):
    Life.all_life.append(self)


class Comment:

  all_comments = []

def __init__(self,title,pitch,user):
  self.title = title
  self.pitch = pitch
  self.comment = comment
  self.user = user

  def save_comment(self):
      comment.all_comments.append(self)

  @classmethod
  def get_pitch(cls):

    response = []

    for pitch in cls.all_businessplans:
      response.append(pitch)

      return response
 
 

  @login_manager.user_loader
  def load_user(user_id):
      return User.query.get(int(user_id))
  







  


    
    