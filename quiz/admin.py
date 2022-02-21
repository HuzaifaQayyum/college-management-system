from datetime import datetime
from django.contrib import admin
from .models import *
from .forms import *


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'gained_marks', 'total_marks', 'date']
    autocomplete_fields = ['student', 'course_subject']
    search_fields = ['student__name__istartswith', 'student__roll_no__exact' ]
    ordering = [ '-date']
    list_filter = ['course_subject']
    form = QuizResultForm
