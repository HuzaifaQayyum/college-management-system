# Generated by Django 4.0.2 on 2022-02-19 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_student_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='join_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
