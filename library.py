from student import *


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []


    def addBook(self, book):
        self.books.append(book)


    def addStudent(self, student):
        self.students.append(student)


    def showBooks(self):
        if not self.books:
            print("There are no books.")
            return

        for book in self.books:
            book.showInfo()
            print("----------------------")


    def showStudents(self):
        if not self.students:
            print("There are no students.")
            return
        
        for student in self.students:
            student.showInfo()
            print("----------------------")



    def searchBook(self, bookID):
        book1 = None
        for book in self.books:
            if book.bookID == bookID:
                book1 = book
                break
            return book1
    def searchStudent(self, studentID):
        student1 = None
        for student in self.students:
            if student.studentID == studentID:
                student1 = student
                break
            return student1
    def borrowBook(self, studentID, bookID):
        student = self.searchStudent(studentID)
        book = self.searchBook(bookID)
        if student and book:
            student.borrowBook(book)
    def returnBook(self, studentID, bookID):
        student = self.searchStudent(studentID)
        book = self.searchBook(bookID)
        if student and book:
            student.returnBook(book)