from dataBaseTable import db, Kitaplar

#create

kitap=Kitaplar("Tabu",2019,"Yelken Yayınevi","Joseph Johnson",6,32)
db.session.add(kitap)
db.session.commit()

#Read
all_books=Kitaplar.query.all() # return list of books
print(all_books)

#Select by ıd
book_one=Kitaplar.query.get(1)
print(book_one)

book_Ucak=Kitaplar.query.filter_by(isim="Uçak")
print(book_Ucak.all())


#Update

first_book=Kitaplar.query.get(1)

first_book.adet=12
db.session.add(first_book)
db.session.commit()




#Delete

second_book=Kitaplar.query.get(2)

db.session.delete(second_book)
db.session.commit()

all_books=Kitaplar.query.all() # return list of books
print(all_books)
