from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'main_page/', views.main, name='main_page'),
    ]