from django import forms
from .models import *


class QuizResultForm(forms.ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['total_marks'] < cleaned_data['gained_marks']:
            raise forms.ValidationError({ 'total_marks': "Total marks can not be smaller than gained marks."})

        return cleaned_data

    class Meta:
        model = QuizResult
        fields = [ 'student', 'course_subject', 'total_marks', 'gained_marks', 'date' ]