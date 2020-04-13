from flask import Flask

from questions.admin.controllers import admin
from questions.config import configure_app
from questions.main import main_bp
from questions.redis_client import redis_client


def create_app():
    """Creates the app with redis instance and Blueprints registered"""
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')
    configure_app(app)
    redis_client.init_app(app)
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(main_bp, url_prefix='/questions')
    app.register_blueprint(admin, url_prefix='/admin')
