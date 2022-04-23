from django.db import models

# Create your models here.

class Employee(models.Model):
    Rollno = models.IntegerField()
    First_name = models.CharField(max_length=30)
    Hint1 = models.CharField(max_length=500)
    Hint2 = models.CharField(max_length=500)
    Secret_Friend = models.IntegerField()
    Hint = models.CharField(max_length=90)
    Task = models.CharField(max_length=90)
    Hint_Friend = models.CharField(max_length=90)
    best_M = models.CharField(max_length=30)
    best_F = models.CharField(max_length=30)
    submit_verfication = models.CharField(max_length=30)
    Total_Gifts = models.IntegerField()
    Gender = models.CharField(max_length=30)
    Hint_3 = models.CharField(max_length=90)
    Hint_4 = models.CharField(max_length=90)
    guess_friend = models.IntegerField()
    guess = models.CharField(max_length=90)

def __str__(self):
    return 'Employee Object with eno: +str(self.no)'