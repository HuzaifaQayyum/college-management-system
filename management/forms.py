from django import forms
from .models import Course, Student, Subject
import re


class CourseForm(forms.ModelForm):

    def clean_name(self):
        return self.cleaned_data['name'].upper()

    class Meta:
        model = Course
        fields = ['name', 'subjects']


class SubjectForm(forms.ModelForm):

    def clean_name(self):
        return self.cleaned_data['name'].title()

    class Meta:
        model = Subject
        fields = ['name']


class StudentForm(forms.ModelForm):

    def clean_roll_no(self):
        roll_no = self.cleaned_data.get('roll_no', '')
        if not re.match('^[0-9]+$', roll_no):
            raise forms.ValidationError("Roll no must only contain digits 0-9.")
        return roll_no


    def clean_name(self):
        return self.cleaned_data['name'].title()


    def clean_phone_no(self):
        number = self.cleaned_data['phone_no']
        if not re.match(r'^0[0-9]{10,12}$', number):
            raise forms.ValidationError('phone number must start with 0 and of length 11-13 integers')
        return number

    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'phone_no', 'course', 'join_date']