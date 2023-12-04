from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, optional

class GuestForm(FlaskForm):
    first_name = StringField('First Name (required)', validators=[DataRequired()])
    last_name = StringField('Last Name (required)', validators=[DataRequired()])
    email = StringField('Email', validators=[optional()])
    attendance = SelectField('Will you be attending? (required)', choices=['Yes', 'No'])
    plus_one = SelectField('Will you be bringing a guest? (required)', choices=['Yes', 'No'])
    guest_first_name = StringField('Guest First Name', validators=[optional()])
    guest_last_name = StringField('Guest Last Name', validators=[optional()])
    dietary_restriction = StringField('Any dietary restrictions?', validators=[optional()])
    comment = TextAreaField('Questions or comments?', validators=[optional()])
    submit = SubmitField('Submit')

class GuestForm_de(FlaskForm):
    first_name = StringField('Vorname (erforderlich)', validators=[DataRequired()])
    last_name = StringField('Nachname (erforderlich)', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[optional()])
    attendance = SelectField('Wirst du dabei sein? (erforderlich)', choices=['Ja', 'Nein'])
    plus_one = SelectField('Wirst du jemanden mitbringen? (erforderlich)', choices=['Ja', 'Nein'])
    guest_first_name = StringField('Gast Vorname', validators=[optional()])
    guest_last_name = StringField('Gast Nachname', validators=[optional()])
    dietary_restriction = StringField('Irgendwelche Essenseinschränkungen?', validators=[optional()])
    comment = TextAreaField('Fragen oder Kommentare?', validators=[optional()])
    submit = SubmitField('Senden')

class GuestForm_tw(FlaskForm):
    first_name = StringField('名（必填）', validators=[DataRequired()])
    last_name = StringField('姓（必填）', validators=[DataRequired()])
    email = StringField('電子郵件', validators=[optional()])
    attendance = SelectField('你會參加嗎？（必填）', choices=['是', '否'])
    plus_one = SelectField('有人同行嗎？（必填）', choices=['是', '否'])
    guest_first_name = StringField('同行 名', validators=[optional()])
    guest_last_name = StringField('同行 姓', validators=[optional()])
    dietary_restriction = StringField('飲食限制？', validators=[optional()])
    comment = TextAreaField('有任何問題嗎?', validators=[optional()])
    submit = SubmitField('提交')