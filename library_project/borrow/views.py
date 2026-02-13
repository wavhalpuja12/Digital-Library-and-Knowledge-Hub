from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from books.models import Book
from .models import BorrowRecord

# ---------- RETURN BOOK ----------
@login_required(login_url='login')
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.is_availible:
        book.is_availible = False
        book.save()

        BorrowRecord.objects.create(
            user=request.user,
            book=book
        )

        messages.success(request, "Book borrowed successfully!")
    else:
        messages.error(request, "Book is not available.")

    return redirect('home')


# ---------- RETURN BOOK ----------
@login_required(login_url='login')
def return_book(request, record_id):
    record = get_object_or_404(BorrowRecord, id=record_id, user=request.user)
    book = record.book

    book.is_availible = True
    book.save()

    record.delete()
    messages.success(request, "Book returned successfully!")

    return redirect('my_books')


# ---------- MY BOOKS ----------
@login_required(login_url='login')
def my_books(request):
    records = BorrowRecord.objects.filter(user=request.user)
    return render(request, 'my_books.html', {'records': records})