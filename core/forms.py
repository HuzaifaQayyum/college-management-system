from django import forms
from .models import Course, Subject


class CourseForm(forms.ModelForm):

    def clean_name(self):
        return self.cleaned_data['name'].upper()


    class Meta:
        model = Course
        fields = [ 'name' ]


class SubjectForm(forms.ModelForm):

    def clean_name(self):
        return self.cleaned_data['name'].upper()


    class Meta:
        model = Subject
        fields = [ 'name', 'course' ]