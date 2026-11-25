import book
from student import *
from book import *
from library import *

class LibraryApp:
        def __init__(self,name):
            self.library = Library(name)

        def menu(self):
            print(
                '''
        ========================= SIMPLE LIBRARY SYSTEM ============================


        ________________________________________________________________________________

        1. ADD BOOK
        2. ADD STUDENT
        3. SHOW ALL BOOKS
        4. SHOW ALL STUDENTS
        5. SEARCH BOOK
        6. SEARCH STUDENT
        7. EXIT
        ________________________________________________________________________________
                '''
            )
        def app(self):
            while True:
                self.menu()
                try:
                    
                        choice = int(input('enter your choice: '))

                        if choice == 1:
                            bookID = int(input('enter book id: '))
                            title = input('enter book title: ')
                            author = input('enter book author: ')
                            pageCount = int(input('enter book page count: '))
                            book = Book(bookID, title, author, pageCount)
                            self.library.addBook(book)


                        elif choice == 2:
                            studentID = int(input("enter student id: "))
                            name = input("enter student name: ")
                            student = Student(studentID, name)
                            self.library.addStudent(student)

                        elif choice == 3:
                            self.library.showBooks()
                            

                        elif choice == 4:
                            self.library.showStudents()

                        elif choice == 5:
                            bookID = int(input("enter book id:"))
                            book = self.library.searchBook(bookID)
                            if book:
                                print(book)
                            else:
                                print("book not found")

                        elif choice == 6:
                            studentID = int(input("enter student id: "))
                            student = self.library.searchStudent(studentID)
                            if student:
                                print(student)
                            else:
                                 print("student not found")
                                

                        elif choice == 7:
                            print('''

            ********************************************************************
                            PROGRAM BAGLANIR
            ********************************************************************
                            ''')
                            break
                except Exception as e:
                    print('xeta bas verdi' ,e)

if __name__ == "__main__":

    library_app = LibraryApp("My Library")
    library_app.app()