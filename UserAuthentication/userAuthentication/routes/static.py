from flask import render_template, Blueprint
from flask_login import login_required

staticView = Blueprint('StaticRoutes',__name__, template_folder='/templates')


@staticView.route('/')
def home():
    return render_template('home.html')

@staticView.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

