from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_user,logout_user,login_required,current_user
from .forms import LoginForm,RegistrationForm,UpdateProfile,BusinessPlan,Interview,LifePitch
from .. import db,photos
from ..models import User,Interview,BusinessPlan,Life
import markdown2


# from ..requests import get_pitch
# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    title = 'pitch out'
    message = 'Add a pitch'
    return render_template('index.html',title=title,message=message)

@main.route('/pitch')
def pitch():
    title = 'pitches'
    
    return render_template('pitch.html',title=title)

@main.route('/interview')
def interview():
    title = 'interview-pitch'
    
    return render_template('interview.html',title=title)

@main.route('/businessplan')
def businessplan():
    title = 'business pitch'
   
    return render_template('business.html',title=title)

@main.route('/life')
def life_pitch():
    title = 'life pitch'
   
    return render_template('life.html',title=title)






@main.route('/pitch/new/<int:id>',methods=['GET','POST'])
@login_required
def new_pitch():
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data

        # Updated pitch instance
        new_pitch = Pitch(pitch_id=pitch.id,pitch_title=title,image_path=pitch.poster,user=current_user)

        # save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.pitch',id = pitch.id ))

        title = 'Home - Get and Make a pitch'
    return render_template(title = title, pitch_form=form, pitch=pitch)
    # pitch = get_pitch(id)
    # title = f'{pitch.title}'

    # business_pitch = get_pitch('business')
    # life_pitch = get_pitch('life')
    # interview_pitch = get_pitch('interview')
    # promotion_pitch = get_pitch('promotion')

   
@main.route('/user/<uname>/update/pic', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
        return render_template('profile/update.html',form =form)
    #pic route
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

    return render_template('profile/update.html',form =form)






    # ,pitch = pitch,business=business,life=life,promotion=promotion,interview=interview)



