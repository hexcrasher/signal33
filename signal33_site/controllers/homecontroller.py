from flask import Blueprint, render_template, request, redirect, url_for

from models import usermodel, addressmodel


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

@ctrl.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = usermodel.UserRegisterModel()
        user.city = request.form['txtCity']
        user.confirm_email_address = request.form['txtConfirmEmailAddress']
        user.email_address = request.form['txtEmailAddress']
        user.first_name = request.form['txtFirstName']
        user.last_name = request.form['txtLastName']
        #user.state = request.form['txtState']
        user.street = request.form['txtStreet']
        user.street2 = request.form['txtStreet2']
        user.user_name = request.form['txtUserName']
        user.zip = request.form['txtZip']

        #TODO: look into secure password handling
        user.password = request.form['txtPassword']
        user.confirm_password = request.form['txtConfirmPassword']
        return redirect(url_for('home.index'))
    return render_template('home/register.html')