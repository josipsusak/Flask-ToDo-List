from wtforms.fields import DateField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


# Create To-DO entry form for database
class EntryForm(FlaskForm):
    todo_text = StringField("Add new", validators=[DataRequired()])
    due_date = DateField('Due date', format='%d-%B-%Y', validators=[DataRequired()])
    submit = SubmitField("Add")


# Create To-Do entry form for viewing
class TodoForm(FlaskForm):
    todo_text = StringField()
    due_date = StringField()
    created_date = StringField()
