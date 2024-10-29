#--- Problem Statement
'''
Implement a Library Management System which will handle the following 

1. Customer should be able to display all the books available in the library
2. Handle the process when a customer requests to borrow a book
3. Update the library collection when a customer returns a book

'''

#-- 
# Class Library -- 
# Layers of Abstraction -- Display availble books, lend a book, add a book

# Class Customer
# Layers of Abstraction -- Request for a Book , Return a book


class Library:
    def displayAvailableBooks(self):
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print('You have borrowed the book ', requestedBook)
            self.availableBooks.remove(requestedBook)
        else:
            print('The Book is not available')


    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have returned the book . Thank You')

    def __init__(self,listOfBook) -> None:
        self.availableBooks = listOfBook

class Customer:
    def requestBook(self):
        print('Enter a name of Book Which you would like to borrow :')
        self.book = input()
        return self.book
    
    def returnBook(self):
        print('Enter a name of Book Which you are returnig : ')
        self.book = input()
        return self.book

library = Library(['ABC','XYZ','MNO'])
customer = Customer()

while True:
    print("Enter 1 to display available books")
    print("Enter 2 to borrow a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    else:
        quit()