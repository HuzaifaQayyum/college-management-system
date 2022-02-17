# Generated by Django 4.0.2 on 2022-02-16 16:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(default=30)),
                ('gained_marks', models.IntegerField()),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.subject')),
            ],
        ),
    ]
