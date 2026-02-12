from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# ---------------- BOOK MODEL ----------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # <-- add this
    is_availible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    book_pdf = models.FileField(upload_to='book_pdfs/', null=True, blank=True)  # if not added yet

    def __str__(self):
        return self.title


# ---------------- BORROW RECORD MODEL ----------------
class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(default=timezone.now)  # <- fixed
    due_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now().date() + timedelta(days=7)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
