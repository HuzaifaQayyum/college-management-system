from django.contrib import admin
from django.utils.html import format_html, urlencode
from .forms import CategoryForm
from django.urls import reverse
from .models import *
from django.contrib.admin.views.main import ChangeList


class CategoryChangeList(ChangeList):

    def get_queryset(self, request):
        depth = None
        try:
            depth = int(request.GET.get('depth', 1))
        except ValueError:
            depth = 1
        finally:
            return super().get_queryset(request).filter(depth=depth)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'edit']
    list_display_links = ['edit']
    search_fields = [ 'name' ]
    
    form = CategoryForm

    def edit(self, category):
        return "Edit"

    @admin.display(description="name")
    def get_name(self, category):
        if category.is_leaf():
            return category.name

        url =   reverse('admin:categories_category_changelist') \
                + '?' \
                + urlencode({ 
                    'depth': str(category.depth + 1),
                    'tree_id': str(category.tree_id)
                })
        return format_html(f'<a href={url}><b>{category.name}</b></a>') 

    def get_changelist(self, request, **kwargs):
        return CategoryChangeList

        