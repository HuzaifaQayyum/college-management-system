# Generated by Django 4.0.2 on 2022-02-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
