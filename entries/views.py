from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import JournalEntry
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from datetime import datetime
from django.contrib.auth.decorators import login_required

class UserListView(generic.ListView):
    template_name = 'auth/user_list.html'
    model = User
    def get_queryset(self):
        return User.objects.all()

#This view should be permissioned. Only superusers should see list of users
#Correction
#from django.contrib.auth.mixins import PermissionRequiredMixin
#class UserListView(PermissionRequiredMixin,generic.ListView):
#    permission_required = "auth.view_user" # be careful with the exact name and prefix
#    template_name = 'auth/user_list.html'
#    model = User
#    def get_queryset(self):
#        return User.objects.all()

class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = 'entries/index.html'
    context_object_name = 'entries_list'

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

@login_required
def new(request):
    je = JournalEntry(user=request.user,journalentry_text=request.POST['entry_text'], entry_date=datetime.now())
    je.save()
    return redirect("/entries/")

class SearchEntriesView(LoginRequiredMixin, generic.ListView):
    template_name = 'entries/search.html'
    context_object_name = 'search_list'
    def get_queryset(self):
        txt = self.request.GET['search_term']
        # see https://stackoverflow.com/questions/3500859/django-request-get
        print(txt)
        print(self.request.user.id)
        with connection.cursor() as cursor:
            print("SELECT journalentry_text FROM entries_journalentry WHERE user_id = '%s' AND journalentry_text LIKE '%%%s%%'" % (self.request.user.id, txt))

            cursor.execute("SELECT journalentry_text, entry_date FROM entries_journalentry WHERE user_id = '%s' AND journalentry_text LIKE '%%%s%%'" % (self.request.user.id, txt))
            resp = cursor.fetchall()
            resp2 = [x[0] + " posted on " + x[1].strftime('%A %d-%m-%Y, %H:%M:%S') for x in resp]
            print(resp2)
            return resp2
#            This is an unsafe way to query the database, open to SQL injection
#            Use rather the following: 
#            resp3 = JournalEntry.objects.filter(user=self.request.user, journalentry_text__contains=txt)
#            resp4 = [x.journalentry_text + " posted on " + x.entry_date.strftime('%A %d-%m-%Y, %H:%M:%S') for x in resp3]
#            print(resp4)
#            return resp4
