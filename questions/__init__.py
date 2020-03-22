from flask import Flask, render_template

from questions.admin.controllers import admin
from questions.config import configure_app
from questions.main.controllers import main

app = Flask(__name__,
            template_folder='templates',)

configure_app(app)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route("/")
def home():
    return render_template("index.htm")


app.register_blueprint(main, url_prefix='/questions')
app.register_blueprint(admin, url_prefix='/admin')
