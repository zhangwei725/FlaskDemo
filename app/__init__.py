from flask import Flask

from app.user.views import init_user

app = Flask(__name__)


def create_app():
    app.debug = True
    register_blue()
    return app


def register_blue():
    init_user(app)
