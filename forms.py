from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class Login(FlaskForm):
	
	username = StringField('Username', validators=[DataRequired(message='Enter fawking username...')])
	password = PasswordField('Password', validators=[DataRequired(message='Enter goddamn password...')])