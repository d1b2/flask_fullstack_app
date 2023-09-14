from flask import Blueprint,render_template

import json


#app config settings
main = Blueprint('main', __name__)




#app routes
@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html',title='Home')

@main.route('/about')
def about():
    return render_template('about.html',title='About')


