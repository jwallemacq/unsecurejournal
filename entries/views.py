from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import JournalEntry
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

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
        if self.request.user.is_superuser:
            return JournalEntry.objects.all()
        else:
            return JournalEntry.objects.filter(user=self.request.user)

