from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from datetime import date
from books.models import Book

# Create your models here.
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
    
class Premium(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()

    def is_active(self):
        return self.expiry_date >= date.today()