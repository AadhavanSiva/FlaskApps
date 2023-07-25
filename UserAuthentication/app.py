from userAuthentication import db,app
from userAuthentication.routes.user import userView
from userAuthentication.routes.static import staticView

app.register_blueprint(userView)

app.register_blueprint(staticView)

if __name__ == '__main__':
    app.run(debug=True)
    