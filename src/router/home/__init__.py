from flask import Flask

from . import home

def init_routes(flask_app: Flask):
    flask_app.add_url_rule("/home", "home", methods=["GET", "POST"], view_func=home.home)
