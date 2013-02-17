from flask import Blueprint, render_template

ctrl = Blueprint('home', __name__)


@ctrl.route('/')
def index():
    return render_template('home/index.html')


@ctrl.route('/about')
def about():
    return render_template('home/about.html')

@ctrl.route('/contact')
def contact():
    return render_template('home/contact.html')

@ctrl.route('/logon')
def logon():
    return render_template('home/logon.html')

@ctrl.route('/register')
def register():
    return render_template('home/register.html')