import math
from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired

class Calculator(FlaskForm):
    video_framerate = StringField('Video Framerate')
    air_time = StringField('Air time', validators=[DataRequired])
    
