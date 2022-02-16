from django.contrib import admin
from django.conf import settings
from .models import *
from .forms import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display    = [ 'name' ]
    form            = CourseForm


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'course']
    form         = SubjectForm
