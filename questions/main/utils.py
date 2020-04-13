import json

from questions import forms
from questions.redis_client import redis_client


def get_questions() -> dict:
    with open('questions/data/questions.json') as data_file:
        questions = json.load(data_file)
        redis_client.hset('questions', 'basic', json.dumps(questions))

    return questions


def get_answer_fields(question) -> dict:
    answer_fields = {}
    for answer in question['answers']:
        name = answer.get('text')
        correct = answer.get('correct')
        answer_fields[answer['id']] = {
            'name': name,
            'correct': correct,
        }
    return answer_fields


def generate_form(request_form) -> forms.QuestionForm:
    if request_form:
        return forms.QuestionForm(request_form)

    form = forms.QuestionForm()
    question = get_questions()[0]
    answer_fields = get_answer_fields(question)

    for answer_id, field in answer_fields.items():
        form.answers.choices.append((answer_id, field['name']))
        redis_client.hset('answer', answer_id, field['correct'])

    form.answers.label = question['title']

    return form
