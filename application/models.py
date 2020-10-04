import flask
from application import db

class Address(db.Model):
    __tablename__ = 'addresses'  #Manual table naming

    addressID   = db.Column(db.Integer, primary_key=True)
    addresss    = db.Column(db.String(120), nullable=False)
    city        = db.Column(db.String(80), nullable=False) 
    state       = db.Column(db.String(80), nullable=False)
    postalCode  = db.Column(db.Integer, nullable=False)
    country     = db.Column(db.String(80), nullable=False)
