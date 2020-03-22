from flask import Blueprint
from flask import render_template

from questions.main import utils

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("index.htm")


@main.route('/all')
def display_questions():
    questions = utils.get_questions()
    return render_template("questions.htm", questions=questions)
