import datetime
import wtforms
from wtforms.validators import length, InputRequired
from models.fansmodels import FansDetailsModel


class FeedbackForm(wtforms.Form):

    username = wtforms.StringField(validators=[length(min=1)])
    opinion = wtforms.StringField(validators=[length(min=1, max=500)])

