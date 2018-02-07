import flask

foodiFeature = flask.Flask(__name__)
foodiFeature.secret_key = 'apple123'


@foodiFeature.route('/')
def index():
    return "Hello!"
