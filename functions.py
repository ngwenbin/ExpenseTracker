from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
import app, re

class UserRegistration(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = StringField('Password',
                           validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = app.User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken, try again')

    def validate_email(self, email):
        user = app.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email taken, try again')

class UserLogin(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=10)])
    password = StringField('Password',
                           validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class NewExpense(FlaskForm):
    category = StringField('Category',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    expense = DecimalField('Expense', validators=[DataRequired(message="Numbers only")])
    submit = SubmitField('Add Expenses')