from flask_wtf import FlaskForm
from wtforms import TimeField, SubmitField, BooleanField
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired


class EditFrom(FlaskForm):
    time = TimeField('Time', validators=[DataRequired()])
    playlist_name = StringField('Playlist\'s name:', validators=[DataRequired()])
    playlist_id = StringField('Playlist\'s URI: ', validators=[DataRequired()])
    submit = SubmitField('Done')
