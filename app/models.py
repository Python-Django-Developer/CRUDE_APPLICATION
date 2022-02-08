from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class TODO(models.Model):
    status_choices=[
        ('C', '✔Completed'),
        ('P', '⏲Pending'),
    ]
    priority_choices = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),

    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=status_choices)

    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choices)
