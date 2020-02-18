from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_pitch,get_pitch
from .forms import ReviewForm
from ..models import Review

@main.route('/')
def index():
    pitch = get_pitch(id)
    title = f'{pitch.title}'

    business_pitch = get_pitch('business')
    life_pitch = get_pitch('life')
    interview_pitch = get_pitch('interview')
    promotion_pitch = get_pitch('promotion')

    title = 'Home - Get and Make a pitch'
    

    return render_template('pitch.html',title = title,pitch = pitch,business=business,life=life,promotion=promotion,interview=interview)
    

