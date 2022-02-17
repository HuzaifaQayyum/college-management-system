from django.contrib import admin
from .models import *
from .forms import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'course']
    list_display_links = ['roll_no', 'name']
    autocomplete_fields = ['course']
    search_fields = ['name']
    form = StudentForm


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
    search_fields = [ 'course__name', 'subject__name' ]

    def get_model_perms(self, *args, **kwargs):
        return { }


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = CourseForm
    inlines = [CourseSubjectinline]
    search_fields = ['name']
