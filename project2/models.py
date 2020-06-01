from flask_login import UserMixin
from flask import Flask
from project2 import db, login_manager
from flask_sqlalchemy import SQLAlchemy


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
