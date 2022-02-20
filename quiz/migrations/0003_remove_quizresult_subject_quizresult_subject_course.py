# Generated by Django 4.0.2 on 2022-02-17 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_coursesubject_unique_together'),
        ('quiz', '0002_quizresult_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='subject',
        ),
        migrations.AddField(
            model_name='quizresult',
            name='subject_course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.coursesubject'),
            preserve_default=False,
        ),
    ]