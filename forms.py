from flask_wtf import FlaskForm
from wtforms import TimeField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class EditFrom(FlaskForm):
    time = TimeField('Time', validators=[DataRequired()])
    active = BooleanField('Active', validators=[DataRequired()])
    submit = SubmitField('Done')
