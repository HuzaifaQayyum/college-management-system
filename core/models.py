from datetime import datetime
from django.db import models


class Course(models.Model):
    name                = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name                = models.CharField(max_length=255)
    course              = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = [ 'name', 'course' ]

    def __str__(self):
        return self.name


class Student(models.Model):
    roll_no             = models.IntegerField()
    name                = models.CharField(max_length=255)
    phone_no            = models.CharField(max_length=13)
    course              = models.ForeignKey(Course, on_delete=models.PROTECT)

    class Meta:
        unique_together = [ 'roll_no', 'course' ]

    def __str__(self):
        return self.name
