from django import forms
from treebeard.forms import movenodeform_factory, MoveNodeForm
from .models import Category


class BaseCategoryForm(MoveNodeForm):

    def clean_name(self):
        return self.cleaned_data.get('name').title()


CategoryForm = movenodeform_factory(Category, form=BaseCategoryForm)
