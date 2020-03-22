from flask import Flask

from questions.admin.controllers import admin
from questions.config import configure_app
from questions.main.controllers import main

app = Flask(__name__)

configure_app(app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
