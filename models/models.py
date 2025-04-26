from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

# Modelos SQLAlchemy
class Employee(db.Model):
    idEmployee = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.BigInteger, nullable=True)
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    activate = db.Column(db.Boolean,nullable=True)
class Hours(db.Model):
    idHours = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Time, nullable=False)

class ServingSalon(db.Model):
    idserving_salon = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    
class Agend(db.Model):
    idAgend = db.Column(db.Integer, primary_key=True)
    Employee_idEmployee = db.Column(db.Integer, db.ForeignKey('employee.idEmployee'), nullable=False)
    Hours_idHours = db.Column(db.Integer, db.ForeignKey('hours.idHours'), nullable=False)
    client = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Float, nullable=True)
    obs = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)

class AgendHasServingSalon(db.Model):
    Servin_Salon_idserving_salon = db.Column(db.Integer, db.ForeignKey('serving_salon.idserving_salon'), primary_key=True)
    Agend_idAgend = db.Column(db.Integer, db.ForeignKey('agend.idAgend'), primary_key=True)
