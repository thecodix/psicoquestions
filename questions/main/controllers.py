from flask import render_template, request 

from questions.main import utils, main_bp


@main_bp.route("/")
def home():
    return render_template("index.htm")


@main_bp.route('/all', methods=['GET', 'POST'])
def display_questions():
    form = utils.generate_form(request.form)
    if request.method == 'POST' and form.validate():
        
        #get the next question
        form = utils.generate_form(request.form)

    return render_template("questions.htm", form=form)


@main_bp.route('404')
def page_not_found(error):
    """ if all route render code 404, redirect to questions.htm"""
    return render_template('questions.htm'), 404
