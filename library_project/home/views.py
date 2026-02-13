from django.shortcuts import render
from books.models import Book
from borrow.models import BorrowRecord
from premium.models import Premium
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    context = {
        'books': books
    }

    if request.user.is_authenticated and request.user.is_superuser:
        context['total_books'] = Book.objects.count()
        context['total_records'] = BorrowRecord.objects.count()

    return render(request, 'home.html', context)


@login_required(login_url='login')
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect('home')

    books = Book.objects.all()
    records = BorrowRecord.objects.all()

    total_books = Book.objects.count()
    available_books = Book.objects.filter(is_availible=True).count()
    total_users = User.objects.count()

    # ✅ Premium System
    premium_count = Premium.objects.count()
    normal_users = total_users - premium_count

    # ✅ Updated Chart Data (Premium vs Normal Users)
    chart_labels = ['Premium Members', 'Normal Users']
    chart_data = [premium_count, normal_users]

    context = {
        'books': books,
        'records': records,
        'total_books': total_books,
        'available_books': available_books,
        'total_users': total_users,
        'premium_count': premium_count,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }

    return render(request, 'admin_dashboard.html', context)