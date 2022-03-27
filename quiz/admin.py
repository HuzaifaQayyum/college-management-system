from django.contrib import admin
from constance import config
from .models import *
from .forms import *



@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'gained_marks', 'total_marks', 'is_pass', 'date']
    autocomplete_fields = ['student', 'course_subject']
    search_fields = ['student__name__istartswith', 'student__roll_no__exact' ]
    ordering = [ '-date']
    list_filter = [ 'course_subject' ]
    form = QuizResultForm

    def subject(self, quiz):
        return quiz.course_subject.subject

    @admin.display(boolean=True)
    def is_pass(self, quiz_result):
        return (quiz_result.gained_marks / quiz_result.total_marks *100) >= config.PASSING_PERCENTAGE
