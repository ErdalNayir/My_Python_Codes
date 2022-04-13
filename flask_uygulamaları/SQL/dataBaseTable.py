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

###############################################

class Kitaplar(db.Model):

    __tablename__="Kitaplar"   #Manual Tabla name

    id=db.Column(db.Integer, primary_key=True) # primary key
    isim=db.Column(db.Text)
    yayinYili=db.Column(db.Integer)
    basimYeri=db.Column(db.Text)
    yazarIsmi=db.Column(db.Text)
    adet=db.Column(db.Integer)
    fiyat=db.Column(db.Integer)
    kacBasim=db.Column(db.Integer)

    def __init__(self,isim,yayinYili,basimYeri,yazarIsmi,adet,fiyat,kacBasim):

        self.isim=isim
        self.yayinYili=yayinYili
        self.basimYeri=basimYeri
        self.yazarIsmi=yazarIsmi
        self.adet=adet
        self.fiyat=fiyat
        self.kacBasim=kacBasim

    def __repr__(self):

        return f"Eklenen kitap bilgileri: {self.isim},{self.yazarIsmi},{self.yayinYili},{self.basimYeri}.  Adet: {self.adet},Fiyat: {self.fiyat}"
