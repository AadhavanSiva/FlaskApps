from userAuthentication import app,db
from flask import render_template,url_for,redirect,request,flash,abort
from flask_login import login_user,login_required, logout_user
from userAuthentication.models import User
from userAuthentication.forms import LoginForm, RegistrationForm



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('you logged out!')
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    app.logger.info("before validate line")

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
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

@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registration!")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    