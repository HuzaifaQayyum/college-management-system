from datetime import datetime
from django.contrib import admin
from .models import *
from .forms import *


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'gained_marks', 'total_marks', 'date']
    autocomplete_fields = ['student', 'course_subject']
    search_fields = ['student__name', 'course_subject__course__name']
    ordering = [ '-date']
    list_filter = ['course_subject']
    form = QuizResultForm


    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_date = datetime.strptime(search_term, '%b %Y')
        except:
            pass
        else:
            queryset |= self.model.objects.filter(date__month__gte=search_term_as_date.month,
                                                  date__month__lt=search_term_as_date.month + 1,
                                                  date__year=search_term_as_date.year)

        return queryset, use_distinct
