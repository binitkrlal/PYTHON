import datetime
import os

class LMs:
    def __init__(self,list_of_books,library_name):
    self.list_of_books = "List_of_books.txt"
    self.library_name = library_name
    self.books_dict = {}
    Id = 101
    with open(self.list_of_books) as bk:
        content = bk.readlines()
    for line in content:
        self.books_dict.update({str(Id)})

