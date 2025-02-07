# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json
from datetime import datetime
import flask
from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import cd_user

from apps.authentication.util import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))

# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if flask.request.method == 'POST':
        # read form data
        email = request.form['email']
        password = request.form['password']
        #return 'Login: ' + username + ' / ' + password
        # Locate user
        user = cd_user.query.filter_by(email=email).first()
        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('authentication_blueprint.route_default'))
        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong email or password',
                               form=login_form)
    if current_user.is_authenticated:
        return redirect(url_for('home_blueprint.index'))
    else:
        return render_template('accounts/login.html',
                               form=login_form) 


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        # # Check usename exists
        # user = cd_user.query.filter_by(email=email).first()
        # if user:
        #     return render_template('accounts/register.html',
        #                            msg='Email already registered',
        #                            success=False,
        #                            form=create_account_form)
        # Check email exists
        user = cd_user.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)
        # else we can create the user
        user = cd_user(**request.form)
        db.session.add(user)
        db.session.commit()
        # Delete user from session
        logout_user()
        return render_template('accounts/register.html',
                               msg='User created successfully.',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login')) 

# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
