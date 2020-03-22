from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Main"

@main.route('questions/')
def display_questions():
    questions = [
        {
            "title": "Question 1?",
            "answers": [
                "True",
                "False",
            ]
        }
    ]

    return render_template("questions.htm", questions=questions)
