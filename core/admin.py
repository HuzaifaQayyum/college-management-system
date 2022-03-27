from django.contrib import admin
from library import models as library_model, admin as library_admin
from management import models as management_model, admin as management_admin
from quiz import models as quiz_model, admin as quiz_admin
from django.db.models.functions import Cast
from django.db import models
from datetime import datetime
from .filters import *


class BorrowAdminWithSearch(library_admin.BorrowAdmin):

    def get_search_fields(self, request):
        return super().get_search_fields(request) + [ 'reader__roll_no__exact' ]


class StudentAdminWithQuizPerformance(management_admin.StudentAdmin):

    def get_list_display(self, request):
        return super().get_list_display(request) + ['overall_average', 'last_month_average']

    def overall_average(self, student):
        return (student.overall_average is not None) and f'{student.overall_average}%' or '-'

    def last_month_average(self, student):
        return (student.lastmonth_average is not None) and f'{student.lastmonth_average}%' or '-'

    def get_queryset(self, request):
        overall_average = Cast(
            Cast(models.Sum('quizresult__gained_marks'), models.FloatField()) /
            models.Sum('quizresult__total_marks') * 100,
            models.IntegerField())

        lastmonth_average = Cast(
            Cast(models.Sum('quizresult__gained_marks', filter=models.Q(quizresult__date__month=datetime.now().month)),
                 models.FloatField()) /
            models.Sum('quizresult__total_marks', filter=models.Q(
                quizresult__date__month=datetime.now().month)) * 100,
            models.IntegerField())

        return super().get_queryset(request).annotate(overall_average=overall_average, lastmonth_average=lastmonth_average)


class QuizResultAdminWithDateFilter(quiz_admin.QuizResultAdmin):

    def get_list_filter(self, request):
        return super().get_list_filter(request) + [  QuizMonthYearFilter ]


admin.site.unregister(library_model.Borrow)
admin.site.register(library_model.Borrow, BorrowAdminWithSearch)

admin.site.unregister(management_model.Student)
admin.site.register(management_model.Student, StudentAdminWithQuizPerformance)

admin.site.unregister(quiz_model.QuizResult)
admin.site.register(quiz_model.QuizResult, QuizResultAdminWithDateFilter)