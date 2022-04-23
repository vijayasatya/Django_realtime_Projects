from django.contrib import admin
from firstApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Rollno', 'First_name', 'Hint1', 'Hint2', 'Secret_Friend', 'Hint', 'Task', 'Hint_Friend', 'best_M', 'best_F','Hint_4', 'submit_verfication', 'Total_Gifts',
    'Gender', 'Hint_3', 'guess_friend','guess']

admin.site.register(Employee,EmployeeAdmin)
