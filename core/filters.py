from django.contrib import admin
from datetime import datetime


class SimpleTextInputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'


    def filter(self, request, queryset, value):
        raise NotImplementedError('Implement this method in subclasses.')


    def queryset(self, request, queryset):
        if self.value() is not None:
            return self.filter(request, queryset, self.value())

    def lookups(self, *args, **kwargs):
        return None

    def has_output(self):
        return True


    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class QuizMonthYearFilter(SimpleTextInputFilter):
    parameter_name = 'date'
    title = 'Quiz (Month Year)'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_holder = 'MM YYYY'

    def filter(self, request, queryset, value):
        try:
            date = datetime.strptime(value, '%b %Y')
        except:
            pass
        else:
            return queryset.filter(date__year=date.year, date__month=date.month)
