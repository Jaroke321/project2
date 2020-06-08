from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    #submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    c_password = PasswordField('Confirm Password',
                               validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class NewChannelForm(FlaskForm):
    channelname = StringField('Channel Name',
                              validators=[DataRequired(), Length(min=2, max=30)])
    is_public = SelectField('Public or Private',
                            choices=[('public', 'Public'), ('private', 'Private')])
    create = SubmitField('Create Channel')
