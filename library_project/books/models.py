from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from datetime import date

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    book_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
    is_availible = models.BooleanField(default=True)

    # 👑 ADD THIS
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title