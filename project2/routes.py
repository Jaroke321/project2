from project2 import app, db
from flask import render_template, url_for, redirect, flash, session, request
from flask_login import login_user, logout_user, login_required, current_user
from project2.forms import LoginForm, RegistrationForm, NewChannelForm
from project2.models import User, Follow, Post, Channel
from flask_socketio import SocketIO, emit


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    """Main page"""

    # If the user is already signed in then send them to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Create the Login Form
    form = LoginForm()
    # Get the js file
    js_file = url_for('static', filename='index.js')
    # User has submitted their credentials
    if form.validate_on_submit():
        # Get the name and password of the user
        name = request.form.get("username")
        password = request.form.get("password")
        # Query the DB for the user first
        user = User.query.filter_by(name=name, password=password).first()
        # Sign the user in if username and password are correct
        if user:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:  # User was not found
            flash('Username or Password is Incorrect', 'danger')
    # Render the sign in page
    return render_template('login.html', js_file=js_file, form=form)


@app.route("/home")
@login_required
def home():
    """Main Page after the login that shows all of 
    the different message channels"""

    js_file = url_for('static', filename='home.js') # Get the correct js file
    # Direct the user to the home page
    return render_template('home.html', js_file=js_file, title="Channeler")


@app.route("/register", methods=['GET', 'POST'])
def register():
    """Register page so that new users can register an account"""

    # Create the form
    form = RegistrationForm()
    # get the javascript file
    js_file = url_for('static', filename='index.js')
    # User has submitted the form
    if form.validate_on_submit():
        # get the values the user entered
        username = form.username.data
        password = form.password.data
        # Create a new user
        new_user = User(name=username, password=password)
        # add user to DB
        db.session.add(new_user)
        db.session.commit()
        flash('You Have Been Successfully Registered, Welcome!!')
        # redirect to the login page
        return redirect(url_for('login'))

    return render_template('register.html', js_file=js_file, form=form)


@app.route("/newChannel", methods=['GET', 'POST'])
@login_required
def newChannel():
    """Allow the user to create a new channel"""

    form = NewChannelForm().  # Create a new channel form

    # Validate the incoming form
    if form.validate_on_submit():
        chan_name = form.channel_name.data
        # emit the new channel to users on the home page
        createChannel()
        # Send the user to the new channels page
        redirect(url_for('channel', chan_name=chan_name))
    # Render the template for a GET request
    return render_template('newChannel.html', form=form)


@app.route("/myChannels")
@login_required
def myChannels():
    """Allows the user to see all of the channels that they have participated in"""


@app.route("/logout")
@login_required
def logout():
    """Logs the current user out"""

    logout_user()  # Logout the current_user
    return redirect(url_for('login'))  # Redirect the user to the login page


def createChannel():
    """When a new channel is being created, this method will process the request
    and when it is complete emit it back to all of the users in real time."""

    # TODO!! This is incomplete, the javascript will check the data and then
    # here is where the new channel will be added to the DB

    channels = Channel.query.all()
    emit("new channel", channels, broadcat=True)
