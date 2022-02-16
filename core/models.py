from datetime import datetime
from django.db import models


class Course(models.Model):
    name                = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name                = models.CharField(max_length=255)
    course              = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    roll_no             = models.AutoField(editable=True)
    name                = models.CharField(max_length=255)
    phone_no            = models.CharField(max_length=13)
    course              = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class QuizResult(models.Model):
    total_marks         = models.IntegerField(default=30)
    gained_marks        = models.IntegerField()
    subject             = models.ForeignKey(on_delete=models.PROTECT)
    date                = models.DateField(default=datetime.now, blank=True)