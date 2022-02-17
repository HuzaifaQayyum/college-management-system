from django.db import models
from django.conf import settings
from datetime import datetime


class QuizResult(models.Model):
    student             = models.ForeignKey(settings.STUDENT_MODEL, on_delete=models.PROTECT)
    course_subject      = models.ForeignKey(settings.COURSE_SUBJECT_MODEL, on_delete=models.PROTECT)
    total_marks         = models.IntegerField(default=30)
    gained_marks        = models.IntegerField()
    date                = models.DateField(default=datetime.now, blank=True)