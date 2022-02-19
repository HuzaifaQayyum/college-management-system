from django.contrib import admin
from django.db.models.functions import Cast
from quiz import models as quiz_models, admin as quiz_admin
from utils.admin import search_by_date, search_by_int
from .models import *
from .forms import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'course',
                    'last_month_average', 'overall_average']
    list_display_links = ['roll_no', 'name']
    list_filter = [ 'course', 'join_date']
    autocomplete_fields = ['course']
    search_fields = ['name__istartswith']
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


    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct =  super().get_search_results(request, queryset, search_term)
        queryset = search_by_int(queryset, search_term, lambda int_term: { 'roll_no__exact': int_term }, self.model)
        return queryset, use_distinct


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


class QuizResultAdminWithSearch(quiz_admin.QuizResultAdmin):

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = search_by_int(queryset, search_term, lambda int_term: {
                                 'student__roll_no__exact': int_term}, self.model)
        queryset = search_by_date(queryset, search_term, lambda date_term: { 'date__month': date_term.month, 'date__year': date_term.year }, model=self.model)
        return queryset, use_distinct


admin.site.unregister(quiz_models.QuizResult)
admin.site.register(quiz_models.QuizResult, QuizResultAdminWithSearch)
