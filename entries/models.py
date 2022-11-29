from django.db import models

class JournalEntry(models.Model):
    journalentry_text = models.CharField(max_length=200)
    entry_date = models.DateTimeField('entry date')

    def __str__(self):
        return self.journalentry_text + " at " + self.entry_date
