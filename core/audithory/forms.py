from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    number = SelectField('ID', coerce=int , validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d' , validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M' , validators=[DataRequired()])
    submit = SubmitField('Book current audithory.')