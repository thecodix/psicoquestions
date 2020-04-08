from wtforms import Form, RadioField, StringField


class QuestionForm(Form):
    answer = RadioField('label', choices=[('value_true','True'),('value_false','False')])

    
