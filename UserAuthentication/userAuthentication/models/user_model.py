from userAuthentication import db,login_manager, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)

class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64),unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        app.logger.info("password_hash =>" + self.password_hash)
        app.logger.info("password =>" + password)

        #return True
        return check_password_hash(self.password_hash,password)

    def emailExists(self, field):
        if UserModel.query.filter_by(email=field.data).first() is None:
            return False
        return True


    def userNameExists(self, field):
        print("check user name " + field.data)
        firstUser = UserModel.query.filter_by(username=field.data).first()
        print(firstUser)
        if firstUser is None:
            #raise ValidationError('Username is taken')
            print("false from check_username")
            return False
        print("true from check_username")
        return True
