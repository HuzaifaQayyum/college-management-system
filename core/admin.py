from django.contrib import admin
from django.conf import settings


@admin.register(settings.STUDENT_MODEL)
class StudentAdmin(admin.ModelAdmin):
    list_display = []

