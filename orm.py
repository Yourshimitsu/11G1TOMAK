from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from init import *

class Predmet(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    kolvo = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f'itemcheck {self.name} {self.cost}'

class Zakaz(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    adres = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    family = db.Column(db.String(80), nullable=False)
    adres = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(80), nullable=False)
    register = db.Column(db.String(80), nullable=False)

class Check(db.Model):
    id_check = db.Column(db.Integer, primary_key=True)
    idorder = db.Column(db.Integer, db.ForeignKey('zakaz.id'), nullable=False)
    order_id = db.relationship('Zakaz', backref=db.backref('Check', lazy=False))
    iduser = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id = db.relationship('User', backref=db.backref('Check', lazy=False))
    iditem = db.Column(db.Integer, db.ForeignKey('predmet.id'), nullable=False)
    item_id = db.relationship('Predmet', backref=db.backref('Check', lazy=False))

class Basket(db.Model):
    id_basket = db.Column(db.Integer, primary_key=True)
    iduser = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id = db.relationship('User', backref=db.backref('Basket', lazy=False))
    iditem = db.Column(db.Integer, db.ForeignKey('predmet.id'), nullable=False)
    item_id = db.relationship('Predmet', backref=db.backref('Basket', lazy=False))

predmet1 = Predmet(id=1, name='1341', kolvo=5, cost=10)
predmet2 = Predmet(id=2, name='1431', kolvo=7, cost=13)
# db.session.add(predmet2)
# db.session.commit()
second_predmet = Predmet.query.all()[1]
print(second_predmet)