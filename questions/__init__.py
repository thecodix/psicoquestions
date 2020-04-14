from flask import Flask, render_template

from questions.admin.controllers import admin
from questions.config import configure_app
from questions.main import main_bp
from questions.redis_client import redis_client


def page_not_found(e):
  """Return template for 404 error."""
  return render_template('404.htm'), 404


def create_app():
    """Creates the app with redis instance and Blueprints registered"""
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.register_error_handler(404, page_not_found)
    configure_app(app)
    redis_client.init_app(app)
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(main_bp, url_prefix='/')
