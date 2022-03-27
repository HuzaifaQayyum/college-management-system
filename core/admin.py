from django.contrib import admin
from library import models as library_model, admin as library_admin
from management import models as management_model, admin as management_admin
from django.db.models.functions import Cast
from django.db import models
from datetime import datetime


class BorrowAdminWithSearch(library_admin.BorrowAdmin):
    search_fields = [ 'book__title', 'book__isbn', 'reader__roll_no__exact'  ]


class StudentAdminWithQuizPerformance(management_admin.StudentAdmin):
    list_display = ['roll_no', 'name', 'course', 'last_month_average', 'overall_average']

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


# admin.site.unregister(library_model.Borrow)
# admin.site.register(library_model.Borrow, BorrowAdminWithSearch)
admin.site.unregister(management_model.Student)
admin.site.register(management_model.Student, StudentAdminWithQuizPerformance)