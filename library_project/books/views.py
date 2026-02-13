from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from premium.models import Premium

# ---------- ADD BOOK (ADMIN ONLY) ----------
@login_required(login_url='login')
def add_book(request):

    if not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST.get('description')
        image = request.FILES.get('image')
        book_pdf = request.FILES.get('book_pdf')
        is_premium = request.POST.get('is_premium') == 'on'

        Book.objects.create(
            title=title,
            author=author,
            description=description,
            image=image,
            book_pdf=book_pdf,
            is_premium=is_premium
        )

        messages.success(request, "Book added successfully!")
        return redirect('admin_dashboard')

    return render(request, 'add_book.html')



# ---------- DELETE BOOK (ADMIN ONLY) ----------
@login_required(login_url='login')
def delete_book(request, book_id):

    if not request.user.is_superuser:
        return redirect('home')

    book = get_object_or_404(Book, id=book_id)
    book.delete()

    messages.success(request, "Book deleted successfully!")
    return redirect('admin_dashboard')



@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.is_premium and not Premium.objects.filter(user=request.user).exists():
        messages.warning(request, "Premium book. Upgrade required.")
        return redirect('upgrade_premium')

    return render(request, 'book_detail.html', {'book': book})
