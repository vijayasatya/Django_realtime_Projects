from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages

from firstApp.models import Employee
import time
import datetime
import wikipedia
import random
import pytz


def home(request):
    return render(request, 'firstapp/home.html')

def login(request):
    if request.method=='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            messages.info(request, 'Invalid Credentials')
            return redirect('/firstApp/login')
        else:
            auth.login(request, x)
            Rollno = request.user.username
            a = Employee.objects.get(Rollno = Rollno)
            rollno = a.Secret_Friend
            b = Employee.objects.get(Rollno = rollno)
            if a.Hint_Friend == '0':
                  a.Hint_Friend = b.Hint2
                  a.save()
            return redirect('/secondApp/main_page')
    else:
          return render(request, 'firstapp/login.html')


def empdata(request):
    emp_list = Employee.objects.all()
    my_dic = {'emp_list' : emp_list}
    return render(request, 'Database/emp.html', context=my_dic)



def add_data(request):
    Rollno = request.user.username
    secret_friend = str(request.POST['secret_friend'])
    a = Employee.objects.get(Rollno = Rollno )
    if a.guess_friend=='0':
       if len(secret_friend)==12:
           a.guess_friend=secret_friend
           a.save()
           messages.info(request,'You updated your guessed number succesfully')
       else:
           messages.info(request,'Invalid Credentials')
    return render(request,'firstapp/main.html')


def logout(request):
    name = request.user.get_short_name()
    auth.logout(request)
    messages.info(request, 'Thank you ' + str(name) + ' !!! if you want you can login again')
    return redirect('/')

def jarvis(request):


    def wiki(query):
        try:
           name = request.user.get_short_name()
           results = wikipedia.summary(query, sentences=2)
        except:
            results = "Sorry "+str(name)+" I don't know about "+str(query)+" you can try another."
        return results

    def wishMe(hour):
        if hour>=0 and hour<12:
            return " Good Morning "
        elif hour>=12 and hour<18:
            w = " Good Afternoon "
        else:
            w = "Good Evening"
        return w
    def Hint3():
        Rollno = request.user.username
        me = Employee.objects.get(Rollno = Rollno)
        friend = me.Secret_Friend
        you = Employee.objects.get(Rollno = friend)
        a = list(str(friend)[11:])
        b = you.Gender
        c = abs(int(Rollno)-int(friend))
        d = you.best_M
        e = you.best_F
        print(a,b,c,d,e)
        z = [a, b, c, d, e]
        result = random.sample(z, 1)
        if me.Hint_4 == '0':
           if result[0] == b:
               if me.Gender == you.Gender:
                   Hint = 'Equal to == '
               else:
                   Hint = ' X Opposite '
           elif result[0] == a:
               Hint = 'A number is:'+str(random.sample(a,1)[0])
           elif result[0] == c:
               if c<20:
                   Hint = 'smaller than 20'
               else:
                   Hint = 'Greater than 20 or equal'
           elif result[0] == d:
               Hint = d
           else:
               Hint = e
           msg = "your Iron-Man hint is --------------"+str(Hint)
           me.Hint_4 = Hint
           me.save()
        else:
            Hint = me.Hint_4
            msg = "your Iron-Man hint is already updated as------------ "+str(Hint)
        return msg

    name = request.user.get_short_name()

    hours = datetime.datetime.now()
    day = hours.strftime("%a,%b %d,%Y")
    tz = pytz.timezone('Asia/kolkata')
    time = hours.astimezone(tz)
    w = wishMe(int(str(time)[10:13]))
    msg = "Hello " + str(name) +" "+ str(w) + " I am Iron-Man and i am back for you to give your hint3.Now enter the password below .If you don't know then get it from secret santa and today is ----------------------------"+str(day)+" and time  "+str(time)[10:19]+" !!!!"
    my_dic = {'msg': msg}
    if request.method == 'POST':
        question_jarvis = request.POST['question_jarvis']
        if question_jarvis == "hint3":
            msg = Hint3()
            messages.info(request, msg)
        else:
           msg = wiki(question_jarvis)
           messages.info(request, msg)
        return render(request, 'firstapp/jarvis.html',context=my_dic)
    else:
        return render(request, 'firstapp/jarvis.html',context=my_dic)


def secret_friend(request):
    return render(request,'firstapp/secret_santa_challenges.html')


def first_hint(request):
        Rollno = request.user.username
        a = Employee.objects.get(Rollno = Rollno)
        messages.info(request, "Your secret friend 1st hint is---------" + str(a.Hint) + "-------")
        return render(request, 'firstapp/main.html')


def Final_Tasks(request):
    Rollno = request.user.username
    a = Employee.objects.get(Rollno = Rollno)
    messages.info(request,'Your challenges are do '+str(a.Task)+'------------ or  do '+str(a.Hint_3))
    return render(request,'firstapp/secret_santa_challenges.html')


def task(request):
    task_friend = request.POST['task1']
    task_friend2 = request.POST['task2']
    Rollno = str(request.user.username)
    b = Employee.objects.get(Secret_Friend=Rollno)
    b.Task = task_friend
    b.Hint_3 = task_friend2
    b.save()
    messages.info(request, "You sent the task ----" + str(task_friend)+" and "+str(b.Hint_3))
    return render(request, 'firstapp/SecretFriendchallenge.html')


def second_hint(request):
    return render(request, 'firstapp/challenges.html')


def Total_Gifts(request):
    Rollno = request.user.username
    a = Employee.objects.get(Rollno=Rollno)
    rollno = a.Secret_Friend
    b = Employee.objects.get(Rollno=rollno)
    if a.submit_verfication == '1':
        if a.guess_friend==a.Secret_Friend:
            a.Total_Gifts+=1
            a.submit_verfication = '0'
            a.save()
            b.Total_Gifts-=1
            b.save()
        else:
            b.Total_Gifts+=1
            b.save()
            a.Total_Gifts-=1
            a.save()
    if a.guess_friend==a.Secret_Friend:
        messages.info(request,"Yes your secret friend is "+str(b.First_name)+"----- he will gifted you")
    else:
        messages.info(request,"No your secret friend is "+str(b.First_name)+"........you need to gifted "+str(b.First_name))

    return render(request, 'firstapp/last.html')

def theme(request):
    return render(request,'firstapp/theme.html')


def completed_challenges(request):
    return render(request,'firstapp/challenges.html')


def Feedback(request):
    about = request.POST['about']
    feedback = request.POST['feedback']
    Rollno = request.user.username
    a = Employee.objects.get(Rollno=Rollno)
    rollno = a.Secret_Friend
    b = Employee.objects.get(Rollno=rollno)
    b.Hint1 = about
    b.save()
    a.Hint2 = feedback
    a.save()
    messages.info(request,"Thank you for your feedback------")
    return render(request,'firstapp/last.html')
















