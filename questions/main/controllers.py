from flask import render_template, request

from questions.main import utils, main_bp
from questions import forms 


@main_bp.route("/")
def home():
    return render_template("index.htm")


@main_bp.route('/all', methods = ['GET','POST'])
def display_questions():
    questions = utils.get_questions()
    form = forms.QuestionForm(request.form)
    if request.method == 'POST':
        print(form.answer.data)

    
    return render_template("questions.htm", questions=questions, form=form)
