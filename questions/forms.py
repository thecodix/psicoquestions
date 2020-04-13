from wtforms import Form, RadioField, validators
from questions.redis_client import redis_client


class QuestionForm(Form):
    answers = RadioField('label', choices=[], validators=[validators.InputRequired()])

    def validate(self):
        if self.errors:
            return False

        answer_id = self.data['answers']
        # TODO this can be better
        if redis_client.hget('answer', answer_id) == b"False":
            return False

        return True

