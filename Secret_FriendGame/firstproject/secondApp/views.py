from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from firstApp.models import Employee


# Create your views here.
def main(request):
    if request.method == 'POST':
        return redirect('/firstApp/empdata')
    else:
        Rollno = request.user.username
        a = Employee.objects.get(Rollno=Rollno)
        #messages.info(request,"Your secret friend 1st hint is---------" + str(a.Hint) + "-------"+"and 2nd hint is......."+str(a.Hint_Friend)+"........"+" and 3rd hint is "+str(a.Hint_4))
        return render(request, 'firstapp/main.html')
