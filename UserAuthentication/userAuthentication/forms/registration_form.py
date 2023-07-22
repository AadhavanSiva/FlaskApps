from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from userAuthentication.models.user_model import UserModel

class RegistrationForm(FlaskForm):
    email =StringField('Email',validators=[DataRequired(), Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must '
                                                                                                     'match !!')])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('register!')



