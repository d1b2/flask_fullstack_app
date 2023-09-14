from flask import Blueprint, render_template,redirect,url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from application import db
from application.models import User
from application.user.wforms import SignupForm, LoginForm
#import json


#user blueprint initialization
user = Blueprint('user', __name__)


#user routes
@user.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
       
        check_user_email_in_db = User.query.filter_by(email=form.email.data).first()
        if check_user_email_in_db :
            flash(f'Please enter different email as {form.email.data} is already taken', 'danger')
            return redirect(url_for('signup'))
        
        check_user_username_in_db = User.query.filter_by(username=form.username.data).first()
        if check_user_username_in_db :
            flash(f'Please enter different username as {form.username.data} is already taken', 'danger')
            return redirect(url_for('user.signup'))
        
        hashed_pwd=generate_password_hash(form.password.data)
        user_created=User(fullname=form.fullname.data,
                          username=form.username.data,
                          dob=form.dob.data,
                          email=form.email.data,
                          password=hashed_pwd)
        db.session.add(user_created)
        db.session.commit()

        new_username=form.fullname.data
        # clear form

        flash(f'Account created for {new_username}!!! Please enter email and password to login', 'success')
        return redirect(url_for('user.login'))
    return render_template('signup.html',form=form)


@user.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.home'))            
            else:
                flash('Login Unsuccessful. Please check the password entered', 'danger')            
        else:
            flash('Login Unsuccessful. Please check email entered', 'danger')
    return render_template('login.html', title='Login', form=form)


@user.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash("You Have Been Logged Out!  Thanks For Stopping By...",'info')
	return redirect(url_for('user.login'))

