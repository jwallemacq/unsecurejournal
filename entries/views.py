from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import JournalEntry
from django.contrib.auth.models import User

class UserListView(generic.ListView):
    template_name = 'auth/user_list.html'
    model = User
    def get_queryset(self):
        return User.objects.all()

#This view should be permissioned. Only superusers should see list of users
#Correction
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
#class UserListView(PermissionRequiredMixin,generic.ListView):
#    permission_required = "auth.view_user" # be careful with the exact name and prefix
#    template_name = 'auth/user_list.html'
#    model = User
#    def get_queryset(self):
#        return User.objects.all()

class IndexView(generic.ListView):
    template_name = 'entries/index.html'
    context_object_name = 'entries_list'

    def get_queryset(self):
        return JournalEntry.objects.all()

