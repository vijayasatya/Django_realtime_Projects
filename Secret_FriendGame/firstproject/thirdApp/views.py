from django.shortcuts import render,redirect
from django.contrib import  messages
from firstApp.models import Employee
from django.http import HttpResponse

# Create your views here.
def final(request):
    if request.method == 'POST':
        return redirect('thirdApp/Final_page')
    else:
        return render(request, 'firstapp/final.html')
def home(request):
    context = {}
    Rollno = request.user.username
    context['Rollno'] = Rollno
    return render(request, 'handcricket/hc.html', context)
