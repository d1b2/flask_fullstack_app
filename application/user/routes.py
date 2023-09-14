from flask import Blueprint, render_template,redirect,url_for,flash
from application.user.wforms import SignupForm, LoginForm
#import json


#user blueprint initialization
user = Blueprint('user', __name__)


#user routes
@user.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('user.login'))
    return render_template('signup.html', title='Signup', form=form)


@user.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'root@admin.com' and form.password.data == 'rootadmin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

