from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from init import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Predmet(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    kolvo = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'itemcheck {self.name} {self.cost}'

class Check(db.Model):
    idorder = db.Column(db.Integer, db.ForeignKey(Zakaz.id), nullable=False)
    order_id = db.relationship('Zakaz', backref=db.backref('Check', lazy=False))
    iduser = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user_id = db.relationship('User', backref=db.backref('Check', lazy=False))
    iditem = db.Column(db.Integer, db.ForeignKey(Predmet.id), nullable=False)
    item_id = db.relationship('Predmet', backref=db.backref('Check', lazy=False))

class Zakaz(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    adres = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

class Basket(db.Model):
    iduser = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user_id = db.relationship('User', backref=db.backref('Basket', lazy=False))
    iditem = db.Column(db.Integer, db.ForeignKey(Predmet.id), nullable=False)
    item_id = db.relationship('Predmet', backref=db.backref('Basket', lazy=False))

class User(db.model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    family = db.Column(db.String(80), nullable=False)
    adres = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(80), nullable=False)
    register = db.Column(db.String(80), nullable=False)