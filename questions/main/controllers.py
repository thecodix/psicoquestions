from flask import render_template

from questions.main import utils, main_bp


@main_bp.route("/")
def home():
    return render_template("index.htm")


@main_bp.route('/all')
def display_questions():
    questions = utils.get_questions()
    return render_template("questions.htm", questions=questions)
