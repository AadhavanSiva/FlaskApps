from userAuthentication import db,app

from flask import Blueprint, render_template,url_for,redirect,request,flash, Blueprint
from flask_login import login_user,login_required, logout_user
from userAuthentication.models.user_model import UserModel
from userAuthentication.forms.login_form import LoginForm

from userAuthentication.forms.registration_form import RegistrationForm

userView = Blueprint('UserRoutes',__name__, template_folder='/templates')

@userView.route("/logout",methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('you logged out!')
    return redirect(url_for('home'))



@userView.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    app.logger.info("before validate line")

    if form.validate_on_submit():
        print("email " + form.email.data)
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user is None:
            return render_template('login.html', form=form,e_error="Email does not exist")
        elif ( user.check_password(form.password.data) == False):
            return render_template('login.html', form=form,p_error="Incorrect password")
        else:
            if( user.check_password(form.password.data) ):
                app.logger.info("after check password")
                login_user(user)
                flash('Logged in Successfully!')
                next = request.args.get('next')


                if next == None or not next[0] == '/':
                    app.logger.info("before welcome_user")
                    next = url_for('welcome_user')
                    app.logger.info("before next/welcome_user redirect")
                return redirect(next)

        app.logger.info("before login template")
    app.logger.info("last line")

    return render_template('login.html',form=form)

@userView.route('/register',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = UserModel(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        if ( user.userNameExists(form.username)):
            return render_template('register.html', form=form, username_message="Username taken")

        if user.emailExists(form.email):
            return render_template('register.html', form=form, email_message="Email already registered")

        db.session.add(user)
        db.session.commit()
        print(".........validation success.....")

        flash("Thanks for registration!")

        return redirect(url_for('login'))
    else:
        print("......validation failed for .....")
    return render_template('register.html',form=form)
