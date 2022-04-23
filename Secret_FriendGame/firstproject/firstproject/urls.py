"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from firstApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'firstApp/', include('firstApp.urls')),
    url(r'secondApp/', include('secondApp.urls')),
    url(r'thirdApp/', include('thirdApp.urls')),
    url(r'^$', views.home),
    url(r'logout/', views.logout, name='logout'),
    url(r'jarvis/', views.jarvis, name='jarvis'),
    url(r'secret_friend/', views.secret_friend, name='secret_friend'),
    url(r'first_hint/', views.first_hint, name='first_hint'),
    url(r'completed_challenges/', views.completed_challenges, name='completed_challenges'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, documeny_root = settings.MEDIA_ROOT)