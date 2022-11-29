from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    journalentry_text = models.CharField(max_length=200)
    entry_date = models.DateTimeField('entry date')

    def __str__(self):
        return self.journalentry_text
