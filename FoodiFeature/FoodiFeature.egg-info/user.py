import flask_login
from FoodiFeature import foodiFeature

login_manager = flask_login.LoginManager()
login_manager.init_app(foodiFeature)

users = {'foo@bar.tld': {'password': 'secret'}}


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    user.is_authenticated = request.form['password'] == users[email]['password']

    return user
