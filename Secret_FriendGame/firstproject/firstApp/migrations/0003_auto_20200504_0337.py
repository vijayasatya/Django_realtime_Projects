# Generated by Django 3.0.5 on 2020-05-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_employee_hint_4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Total_Gifts',
        ),
        migrations.AddField(
            model_name='employee',
            name='guess_friend',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
