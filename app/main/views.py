from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm,RegistrationForm
from ..models import User


# from ..requests import get_pitch
# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    # pitch = get_pitch(id)
    # title = f'{pitch.title}'

    # business_pitch = get_pitch('business')
    # life_pitch = get_pitch('life')
    # interview_pitch = get_pitch('interview')
    # promotion_pitch = get_pitch('promotion')

    title = 'Home - Get and Make a pitch'

@main.route('/login', methods = ['GET','POST'])
@login_required
def login():
    login_user()
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    render_template('profile/profile.html',user = user)





@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    

    return render_template('pitch.html',title = title)
    # ,pitch = pitch,business=business,life=life,promotion=promotion,interview=interview)



