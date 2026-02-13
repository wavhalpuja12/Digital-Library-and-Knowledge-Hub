from django.urls import path
from . import views

urlpatterns = [
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:record_id>/', views.return_book, name='return_book'),
    path('my-books/', views.my_books, name='my_books'),
]
