from flask import Flask, render_template,redirect,url_for,flash
from wforms import SignupForm, LoginForm
import json


#app config settings
app = Flask(__name__, template_folder='templates', static_folder='static')
with open('secrets/secrets.json') as secret:
        app_info=json.load(secret)

app.config['SECRET_KEY'] = app_info['secret_key']


#app routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Signup', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'root@admin.com' and form.password.data == 'rootadmin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug = True)