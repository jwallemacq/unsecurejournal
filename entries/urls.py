from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('users/',views.UserListView.as_view(), name="users"), 
] 
