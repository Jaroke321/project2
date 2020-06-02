from project2 import app, db
from flask import render_template, url_for, redirect, flash, session, request
from flask_login import login_user, logout_user, login_required, current_user
from project2.forms import LoginForm, RegistrationForm
from project2.models import User


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    """Main page"""

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Create the Login Form
    form = LoginForm()
    # Get the js file
    js_file = url_for('static', filename='index.js')

    if form.validate_on_submit():

        name = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(name=name, password=password).first()

        if user:
            login_user(user, remember=form.remember.data)
            redirect(url_for('home'))

    return render_template('login.html', js_file=js_file, form=form)


@app.route("/home")
@login_required
def home():
    """Main Page after the login that shows all of 
    the different message channels"""

    js_file = url_for('static', filename='home.js')

    return render_template('home.html', js_file=js_file)


@app.route("/register")
def register():
    """Register page so that new users can register an account"""


@app.route("/newChannel", methods=['GET', 'POST'])
@login_required
def newChannel():
    """Allow the user to create a new channel"""

@app.route("/myChannels")
@login_required
def myChannels():
    """Allows the user to see all of the channels that they have participated in"""


@app.route("/logout")
@login_required
def logout():
    """Logs the current user out"""

    logout_user()

    return redirect(url_for('login'))
