# Generated by Django 3.2 on 2022-02-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_student_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='course title'),
        ),
    ]
