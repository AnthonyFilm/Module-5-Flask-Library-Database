from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo



class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()


class RegistrationForm(UserLoginForm):
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    def is_registrationform(self):
        if isinstance(self, 'RegistrationForm'):
            return True
        else:
            return False