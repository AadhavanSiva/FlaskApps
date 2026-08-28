import os
from flask import Blueprint, g,Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
#from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
import MySQLdb.cursors

login_manager = LoginManager()
global app
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('AUTHENTICATION_SECRET_KEY')
basedir = os.path.abspath(os.path.dirname(__file__))

mysqlLoginId = os.environ.get('authentication.mysql.login.id')
mysqlLoginPassword = os.environ.get('authentication.mysql.login.password')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + mysqlLoginId + ":" + mysqlLoginPassword + "@localhost/authentication"

app.secret_key = os.environ.get('AUTHENTICATION_SECRET_KEY')

app.config['MYSQL_HOST'] = os.environ.get('AUTHENTICATION_MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('authentication.mysql.login.id')
app.config['MYSQL_PASSWORD'] = os.environ.get('authentication.mysql.login.password')
app.config['MYSQL_DB'] = os.environ.get('AUTHENTICATION_MYSQL_DB', 'authentication')

db = SQLAlchemy(app)

login_manager.init_app(app)
login_manager.login_view = 'login'


logging.basicConfig(level=logging.DEBUG)