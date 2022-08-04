from django.urls import path
from unicodedata import name

from .views.AddBook import AddBookApiview
from .views.AvailableBooks import AvailableBooksApiview
from .views.DeleteBook import DeleteBookApiview
from .views.IssueBook import IssueBookApiview
from .views.ReturnBook import ReturnBookApiview
from .views.UpdateBook import UpdateBookApiview

urlpatterns = [
    path('insert/',AddBookApiview, name="insertBook"),
    path('view/', AvailableBooksApiview, name="viewBooks"),
    path('borrow/<int:pk>', IssueBookApiview, name="borrowBook"),
    path('return/<int:pk>', ReturnBookApiview, name="returnBook"),
    path('update/<int:pk>', UpdateBookApiview, name="updateBook"),
    path('delete/<int:pk>', DeleteBookApiview, name="deleteBook"),
]