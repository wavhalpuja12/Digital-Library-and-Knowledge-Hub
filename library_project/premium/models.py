from django.db import models
from django.contrib.auth.models import User

class Premium(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='premium_account'
    )
    activated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

