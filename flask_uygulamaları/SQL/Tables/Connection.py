import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite') # directory for database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # to prevent to track all changes of SQLALCHEMY_DATABASE_URI

db=SQLAlchemy(app)

Migrate(app,db)

class Kopekler(db.Model):

    __tablename__="Köpekler"

    id=db.Column(db.Integer, primary_key=True) # primary key
    isim=db.Column(db.Text)


    oyuncak=db.relationship("Oyuncaklar",backref="kopekler",lazy="dynamic") # One to many connecting Kopekler table with Oyuncaklar table one dog has many toys

    sahip=db.relationship("Sahip",backref="kopekler",uselist=False) #One to One relationship between kopekler and Sahip table

    def __init__(self,isim):

        self.isim=isim

    def __repr__(self):
        if self.sahip:
            return f"Dog name is {self.isim} and Owner is {self.sahip.name}"
        else:
            return f"Dog name is {self.isim} and Dog has no owner yet!"

    def report_toys(self):

        print("Here are my toys")

        for toy in self.oyuncak:

            print(toy.oyuncak_ismi)

class Oyuncaklar(db.Model):

    __tablename__="Oyuncaklar"

    id=db.Column(db.Integer, primary_key=True)
    oyuncak_ismi=db.Column(db.Text)

    puppy_id=db.Column(db.Integer,db.ForeignKey('Köpekler.id')) # connecting with Köpekler table

    def __init__(self,oyuncak_ismi,puppy_id):

        self.oyuncak_ismi=oyuncak_ismi
        self.puppy_id=puppy_id



class Sahip(db.Model):

    __table_name__="Sahipler"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)

    puppy_id=db.Column(db.Integer,db.ForeignKey('Köpekler.id'))  # connecting with Köpekler table

    def __init__(self,name,puppy_id):

        self.name=name
        self.puppy_id=puppy_id
