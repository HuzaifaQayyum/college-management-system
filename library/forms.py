from django import forms
from django.db import models
import re
from library.models import Book, Author


class AuthorForm(forms.ModelForm):

    def clean_name(self):
        return self.cleaned_data.get('name').title()

    class Meta:
        model = Author
        fields = [ 'name' ]


class BorrowForm(forms.ModelForm):
    
    def save(self, *args, **kwargs):

        if ('book' in self.changed_data) and (self.initial and self.initial['book'] != self.cleaned_data['book'].pk ):
            Book.objects.filter(pk=self.initial['book']).update(assigned=models.F('assigned') - 1)
        if 'book' in self.changed_data:
            Book.objects.filter(pk=self.cleaned_data['book'].pk).update(assigned=models.F('assigned') + 1)
        return super().save(*args, **kwargs);
    
    
class BookForm(forms.ModelForm):

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not re.match('^[0-9]{13}$', isbn):
            raise forms.ValidationError("ISBN must contain only digits of 13 characters.")

        return self.cleaned_data.get('isbn')


    def clean(self):
        cleaned_data = super().clean()
        if 'title' in self.changed_data or 'author' in self.changed_data:
            book_already_exists = Book.objects.filter(title__iexact=cleaned_data['title']) \
                        .annotate(authors_count=models.Count('author')) \
                        .filter(authors_count=cleaned_data['author'].count()) \
                        .filter(author__in=cleaned_data['author']).exists()
                        
            if book_already_exists:
                raise forms.ValidationError("Book with same title and same list of authors already exists.")

        return cleaned_data
        