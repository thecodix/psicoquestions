from wtforms import Form, RadioField, StringField


class QuestionForm(Form):
        
    answer = RadioField('Label', choices=[('value','True'),('value2','False')])

    
