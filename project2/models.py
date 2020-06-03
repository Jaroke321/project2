from flask_login import UserMixin
from flask import Flask
from project2 import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    """Association Table between User and Channel"""
    id = db.Column(db.Integer, primary_key=True)
    chan_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    user_name = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    channel = db.relationship("Channel", back_populates="posts")


class Follow(db.Model):
    """Association Table between the users and channels"""
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    chan_id = db.Column(db.Integer, db.ForeignKey('channel.id'), primary_key=True)

    channel = db.relationship("Channel", back_populates="followers")
    user = db.relationship("User", back_populates="following")


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    following = db.relationship("Follow", back_populates="user")


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(40), nullable=False)
    admin_id = db.Column(db.Integer, nullable=True, default=None)
    public = db.Column(db.Boolean(), nullable=False, default=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    posts = db.relationship("Post", back_populates="channel")
    followers = db.relationship("Follow", back_populates="channel")
