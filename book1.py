
class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year

# __str__ or __repr__  

    def __str__(self)  :
        return f"{self.title} by {self.author}, {self.year}"
    

class Library:
    def __init__(self) :
        self.books = ['yya', 'nooo', "2002", "asdf21"]

    def add_book (self, book):
        self.books.append(book)
        print(f"Book: {book} is added to Library. " )

    def view_book(self):
        # print(self.books)
        print("*" * 20)
        print("Books In Library")
        for index, value in enumerate(self.books, 1):
            print(f"{index}. {value}")

    def del_book(self, option):

        if (option > self.books.__len__()) | (option < 0):
            print("Invalid Book Numbr")
        else:
            print(f"{self.books[option]}  is removed from the list")
            self.books.pop(option)

    def search_book(self, bookname):
        
        for i,v in  enumerate(self.books):            
            if bookname.lower() in self.books[i].lower():
                print(f"{i}. {v}")

        

def option():
    library = Library()
    while (True):
        print('-' * 20)
        print("1. View Book")
        print("2. Add Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Quit App")
        print('-' * 20)
        choice = input("Choose Your Option: ")
        # choice = '4'

        match choice:
            case '1': 
                library.view_book()
            case '2':
                book = input("Enter Book Name: ")
                library.add_book(book)
            case '3': 
                library.view_book()
                option = int(input("Book No. You want to Delete: "))
                library.del_book((option-1))
                library.view_book()
                

            case '4':
                bookname = input("Enter Book Name: ")
                library.search_book(bookname)
            case '5':
                break
            case _:
                print("Invalid Choice")
        # print('-' * 20)


        
        



if __name__ == "__main__":
    option()
    