from Connection import db,Kopekler,Sahip,Oyuncaklar


# Creating dogs
komur=Kopekler("Kömür")
boncuk=Kopekler("Boncuk")

# Adding them to db

db.session.add_all([komur,boncuk])
db.session.commit()

#check
print(Kopekler.query.all())

komur=Kopekler.query.filter_by(isim="Kömür").first()
print (komur)

# creating owner object

erdal=Sahip("Erdal",komur.id)

#Kömür toys

toy1=Oyuncaklar("Kemik",komur.id)
toy2=Oyuncaklar("Frizbi",komur.id)

db.session.add_all([erdal,toy1,toy2])
db.session.commit()

# grab komur again
komur=Kopekler.query.filter_by(isim="Kömür").first()
print (komur)



komur.report_toys()
