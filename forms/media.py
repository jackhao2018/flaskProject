import datetime
import wtforms
from wtforms.validators import length, InputRequired


class MediaForm(wtforms.Form):

    title = wtforms.StringField(validators=[length(min=5, max=100)])
    addr = wtforms.StringField(InputRequired())
    type = wtforms.IntegerField(InputRequired())
