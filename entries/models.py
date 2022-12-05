from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    journalentry_text = models.CharField(max_length=200)
    entry_date = models.DateTimeField('entry date')
    sensitive_data = encrypt(models.CharField(max_length=10, default="hello"))

    def __str__(self):
        return self.journalentry_text
