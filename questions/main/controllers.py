from flask import render_template, request 

from questions.main import utils, main_bp


@main_bp.route("/")
def home():
    return render_template("index.htm")


@main_bp.route('/all', methods=['GET', 'POST'])
def display_questions():
    form = utils.generate_form(request.form)
    return render_template("questions.htm", form=form)
