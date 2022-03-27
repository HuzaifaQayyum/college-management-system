from datetime import datetime
from django.db import models
from .managers import SubjectManager, CourseManager


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)

    objects = SubjectManager()

    def natural_key(self):
        return [ self.name ]

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField("course title", max_length=255, unique=True)
    subjects = models.ManyToManyField(Subject, related_name='courses', through='CourseSubject')

    objects = CourseManager()

    def natural_key(self):
        return [ self.name ]

    def __str__(self):
        return self.name


class CourseSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name} - {self.subject.name}"

    class Meta:
        unique_together = [ 'subject', 'course' ]


class Student(models.Model):
    roll_no = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=13, unique=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    join_date = models.DateField(default=datetime.now)

    class Meta:
        unique_together = ['roll_no', 'course']

    def __str__(self):
        return self.name
