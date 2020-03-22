from flask import Flask
from questions.redis_client import redis_client

from questions.admin.controllers import admin
from questions.config import configure_app
from questions.main.controllers import main


def create_app():
    """Creates the app with redis instance and Blueprints registered"""
    app = Flask(__name__,
                template_folder='templates',)
    configure_app(app)
    redis_client.init_app(app)
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(main, url_prefix='/questions')
    app.register_blueprint(admin, url_prefix='/admin')
