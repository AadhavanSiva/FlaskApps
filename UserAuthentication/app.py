from userAuthentication import db,app

from flask import render_template,url_for,redirect,request,flash
from flask_login import login_user,login_required, logout_user
from userAuthentication.models.user_model import UserModel
from userAuthentication.forms.login_form import LoginForm

from userAuthentication.forms.registration_form import RegistrationForm

from userAuthentication.routes.user import userView

app.register_blueprint(userView)




if __name__ == '__main__':
    app.run(debug=True)
    