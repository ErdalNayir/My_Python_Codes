from dataBaseTable import db, Kitaplar

db.create_all()




kasagi=Kitaplar("Kaşağı",2001,"Can Yayınevi","Ömer Seyfettin",5,12)
ucak=Kitaplar("Uçak",2018,"Epsilon Yayınevi","Emre Nayir",3,25)

print(kasagi.id)
print(ucak.id)

db.session.add_all([kasagi,ucak])

db.session.commit()

print(kasagi.id)
print(ucak.id)
