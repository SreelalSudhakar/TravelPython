from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.operation,name="operation"),
    path('details',views.details,name="details"),
    path('thanks',views.thanks,name="thanks"),
    ]