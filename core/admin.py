from django.contrib import admin
from django.db.models.functions import Cast
from library import models as library_model, admin as library_admin
from .models import *
from .forms import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'course',
                    'last_month_average', 'overall_average']
    list_display_links = ['roll_no', 'name']
    list_filter = [ 'course__name', 'join_date']
    autocomplete_fields = ['course']
    search_fields = ['name__istartswith', 'roll_no__exact']
    ordering = ['roll_no']
    form = StudentForm

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



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = SubjectForm
    search_fields = ['name']
    ordering = ['name']


class CourseSubjectinline(admin.TabularInline):
    model = CourseSubject
    autocomplete_fields = ['subject']
    extra = 1


@admin.register(CourseSubject)
class CourseSubjectAdmin(admin.ModelAdmin):
    search_fields = ['course__name', 'subject__name']

    def get_model_perms(self, *args, **kwargs):
        return {}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = CourseForm
    inlines = [CourseSubjectinline]
    search_fields = ['name']


class BorrowAdminWithSearch(library_admin.BorrowAdmin):
    search_fields = [ 'book__title', 'book__isbn', 'reader__roll_no'  ]


admin.site.unregister(library_model.Borrow)
admin.site.register(library_model.Borrow, BorrowAdminWithSearch)