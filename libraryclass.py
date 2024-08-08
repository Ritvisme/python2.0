#Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from\
 #       this Library class and show how you can print all books, add a book and get the number of books using different
#methods. Show that your program doesnt persist the books after the program is stopped!
class Library():
    def __init__(self):
        self.numbooks=0
        self.books=[]
    def addbooks(self,book):
        self.books.append(book)
        self.numbooks=len(self.books)
    def info(self):
        print(f"the number of books is {self.numbooks}")
l1=Library()
l1.addbooks("HARRY POTTER")
l1.addbooks("RICK RIORDAN")
l1.addbooks("HOW TO WIN OVER FRIENDS AND INFLUENCE PEOPLE")
l1.addbooks("THINK LIKE A MONK")
l1.info() 
