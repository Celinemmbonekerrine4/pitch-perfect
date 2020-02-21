from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User



class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    confirm_password = PasswordField('Password',validators =[Required()])
    submit = SubmitField('Sign Up')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class Interview(FlaskForm):

    title = StringField('Interview title',validators=[Required()])
    pitch = TextAreaField('Interview pitch',validators=[Required()])
    submit = SubmitField('Submit')


class BusinessPlan(FlaskForm):

    title = StringField('Business plan title',validators=[Required()])
    pitch = TextAreaField('Business plan pitch',validators=[Required()])
    submit = SubmitField('Submit')

class LifePitch(FlaskForm)  :
    title = StringField('Life-pitch title',validators=[Required()])
    pitch = TextAreaField('Life-pitch pitch',validators=[Required()])
    submit = SubmitField('Submit')
    
class Comments(FlaskForm):
    comments = TextAreaField('Any Comments??',validators=[Required()])
    submit = SubmitField('Comments...')

