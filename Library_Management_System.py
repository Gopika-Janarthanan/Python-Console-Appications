class Author:
    def __init__(self, name, dob, nationality):
        self.name = name
        self.dob = dob
        self.nationality = nationality

class Publisher:
    def __init__(self, name,location):
        self.name = name
        self.location = location

class Book:
    def __init__(self, author, publisher,title, isbn, genre, price):
        self.author = author
        self.publisher = publisher
        self.title = title
        self.isbn = isbn
        self.genre = genre
        self.price = price
        

class EBook(Book):
    def __init__(self,author, publisher,title, isbn, genre, price, file_format):
        super().__init__(author, publisher,title, isbn, genre, price)
        self.file_format = file_format

    def display(self):
        super().display()
        print("File Format:", self.file_format)

a = Author("Gopika", "28-06-2004", "Indian")
p = Publisher("J G pubication", "India - Tamil nadu")
b1 = Book( a, p,"Dream",12345 , "fantacy"," Rs.2999")
e1 = EBook(a, p,"fly", 56789, "fantacy", " Rs.1999", "PDF")

print("Book Information")
print("Title:", b1.title)
print("Price:", b1.price)
print("ISBN:", b1.isbn)
print("Genre:", b1.genre)
print("Author:", b1.author.name)
print("Author DOB :",b1.author.dob)
print("Author Nationality :",b1.author.nationality)
print("Publisher:", b1.publisher.name)
print("Publisher Location:", b1.publisher.location)


print()
print("EBook Information:")
print("Title:", e1.title)
print("Price:", e1.price)
print("ISBN:", e1.isbn)
print("Genre:", e1.genre)
print("Author:", e1.author.name)
print("Author DOB :",e1.author.dob)
print("Author Nationality :",e1.author.nationality)
print("Publisher:", e1.publisher.name)
print("Publisher Location:", e1.publisher.location)
print("File Format:", e1.file_format)

------------------------------------

OUTPUT:

Book Information
Title: Dream
Price:  Rs.2999
ISBN: 12345
Genre: fantacy
Author: Gopika
Author DOB : 28-06-2004
Author Nationality : Indian
Publisher: J G pubication
Publisher Location: India - Tamil nadu

EBook Information:
Title: fly
Price:  Rs.1999
ISBN: 56789
Genre: fantacy
Author: Gopika
Author DOB : 28-06-2004
Author Nationality : Indian
Publisher: J G pubication
Publisher Location: India - Tamil nadu
File Format: PDF
