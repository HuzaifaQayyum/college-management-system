# Generated by Django 4.0.2 on 2022-02-17 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_coursesubject_unique_together'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresult',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.student'),
            preserve_default=False,
        ),
    ]