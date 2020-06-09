from project2 import app, db
from flask import render_template, url_for, redirect, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from project2.forms import LoginForm, RegistrationForm, NewChannelForm
from project2.models import User, Follow, Post, Channel
from sqlalchemy import *

import time


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    """Main page"""

    # If the user is already signed in then send them to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Get the js file
    js_file = url_for('static', filename='login.js')
    # User has submitted their credentials
    if request.method == 'POST':
        # Get the name and password of the user
        name = request.form.get("username")
        password = request.form.get("password")
        # Query the DB for the user first
        user = User.query.filter_by(name=name, password=password).first()
        # Sign the user in if username and password are correct
        if user:
            login_user(user)
            return redirect(url_for('home'))
        else:  # User was not found
            flash('Username or Password is Incorrect', 'danger')
            return render_template('login.html', js_file=js_file), 400
    # Render the sign in page
    return render_template('login.html', js_file=js_file)


@app.route("/home")
@login_required
def home():
    """Main Page after the login that shows all of
    the different message channels"""

    js_file = url_for('static', filename='home.js')  # Get the correct js file

    channels = Channel.query.all()
    # Direct the user to the home page
    return render_template('home.html', js_file=js_file, title="Channeler", channels=channels)


@app.route("/register", methods=['GET', 'POST'])
def register():
    """Register page so that new users can register an account"""

    # get the javascript file
    js_file = url_for('static', filename='register.js')
    # User has submitted the form
    if request.method == 'POST':
        # get the values the user entered
        username = request.form.get()
        password = request.form.get()

        # Query to see if the user already exists
        user = User.query.filter_by(name=username).first()

        # Add the user to the DB if the name is not taken
        if not user:
            # Create a new user
            new_user = User(name=username, password=password)
            # add user to DB
            db.session.add(new_user)
            db.session.commit()
            flash('You Have Been Successfully Registered, Welcome!!')
            # redirect to the login page
            return redirect(url_for('login'))

    return render_template('register.html', js_file=js_file)


@app.route("/newChannel", methods=['GET', 'POST'])
@login_required
def newChannel():
    """Allow the user to create a new channel"""

    js_file = url_for('static', filename='createChannel.js')  # Get the correct JS file

    # Validate the incoming form
    if request.method == 'POST':
        # Get the channel name thatthe user is submitting
        chan_name = request.form.get('channel_name')
        # Query to see if the channel name already exists
        chan = Channel.query.filter_by(channel_name=chan_name).first()

        # Add new channel to the DB if it does not already exist
        if not chan:
            channel = Channel(channel_name=chan_name, admin_id=current_user.id)
            db.session.add(channel)
            db.session.commit()

        redirect(url_for('home'))
    # Render the template for a GET request
    return render_template('newChannel.html', js_file=js_file)


@app.route("/search", methods=['POST'])
def search():
    """This function will be used by the search bar on the home page to retrieve channel names actively"""

    # Get the incoming text that the user is searching for
    incoming = "%" + request.form.get("text") + "%"

    q = Channel.query.filter(Channel.channel_name.ilike(incoming)).all()

    for c in q:
        print(c.channel_name)

    return jsonify(incoming)


@app.route("/myChannels")
def myChannels():
    """Allows the user to see all of the channels that they have participated in"""

    return render_template('myChannels.html')


@app.route("/logout")
@login_required
def logout():
    """Logs the current user out"""

    logout_user()  # Logout the current_user
    return redirect(url_for('login'))  # Redirect the user to the login page


@app.route("/channels", methods=['POST'])
def channels():
    """This route is used by the home page so that the user
    can retrieve all the correct channels in increments of 20"""

    # Get the offset and the limit for the query
    offset = int(request.form.get("offset") or 0)
    limit = int(request.form.get("limit"))

    # Query the DB for the channels with offset and limit
    data = [ch.channel_name for ch in Channel.query.offset(offset).limit(limit).all()]

    # Return the JSON data
    return jsonify(data)
