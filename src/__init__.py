import flask
import flask_login

app = flask.Flask(__name__)
app.secret_key = 'apple123'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from src.authentication.AuthAPI import authentication_api

app.register_blueprint(authentication_api)
