from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'Final_page/', views.final),
    url(r'Hand_Cricket/', views.home, name = 'Hand_Cricket'),
    ]