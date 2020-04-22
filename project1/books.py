import os
import csv
from bookdb import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    Base.metadata.create_all(bind = engine)
    file = open("books.csv")
    reader = csv.reader(file)
    next(reader)
    for isbn,title,author,year in reader:
        book = Books(isbn= isbn,title= title, author = author, year = int(year))
        db.add(book)
    db.commit()
    db.close()   

if __name__=="__main__":
    main()     