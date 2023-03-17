from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, Length, email_validator


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(), Length(min=5, max=150)])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=10)])
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("SIGN UP")
