# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    email = StringField('Email',
                         id='email',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='password',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    first_name = StringField('First Name',
                         id='first_name',
                         validators=[DataRequired()])
    last_name = StringField('Last Name',
                         id='last_name',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='password',
                             validators=[DataRequired()])
