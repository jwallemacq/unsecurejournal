from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import JournalEntry

class IndexView(generic.ListView):
    template_name = 'entries/index.html'
    context_object_name = 'entries_list'

    def get_queryset(self):
        return JournalEntry.objects.all()

