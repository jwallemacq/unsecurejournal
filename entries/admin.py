from django.contrib import admin

# Register your models here.

from .models import JournalEntry

admin.site.register(JournalEntry)
