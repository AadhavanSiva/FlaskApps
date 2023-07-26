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

app.config['SECRET_KEY'] = 'msk'
basedir = os.path.abspath(os.path.dirname(__file__))

mysqlLoginId = os.environ.get('authentication.mysql.login.id')
mysqlLoginPassword = os.environ.get('authentication.mysql.login.password')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + mysqlLoginId + ":" + mysqlLoginPassword + "@localhost/authentication"

app.secret_key = '1sdfs423ad'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admin123'
app.config['MYSQL_DB'] = 'authentication'

db = SQLAlchemy(app)

login_manager.init_app(app)
login_manager.login_view = 'login'


logging.basicConfig(level=logging.DEBUG)