from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'login', views.login),
    url(r'empdata/', views.empdata),
    url(r'add_data/', views.add_data, name='add_data'),
    url(r'task/', views.task, name='task'),
    url(r'second_hint/', views.second_hint, name='second_hint'),
    url(r'Total_Gifts/', views.Total_Gifts, name='Total_Gifts'),
    url(r'theme/', views.theme,name = 'theme'),
    url(r'Final_Tasks/', views.Final_Tasks,name = 'Final_Tasks'),
    url(r'Feedback/', views.Feedback,name = 'Feedback'),

    ]