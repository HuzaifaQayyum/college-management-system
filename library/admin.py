from django.contrib import admin
from django.db import models
from django.http.response import HttpResponseRedirect
from django.urls import path, reverse
from library.forms import BookForm, BorrowForm, AuthorForm
from .models import Book, Author, Borrow
from django.utils.html import format_html
from django.utils.http import urlencode


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'books' ]
    form = AuthorForm
    search_fields = [ 'name' ]
    
    def books(self, author):
        if author.book_count:
            return format_html('<a href="{}">{}</a>', 
                            reverse('admin:library_book_changelist') + '?' + urlencode({'author': author.id}), 
                            author.book_count)

        return author.book_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(book_count=models.Count('book'))


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_preview', 'category',  'stock', 'is_available' ]
    search_fields =  [ 'name__istartswith', 'author__name__istartswith', 'isbn__startswith' ]
    autocomplete_fields = [ 'category', 'author' ]
    form = BookForm
        
    def book_preview(self, book):
        return format_html('<img src="{}" class="image_preview" alt="Image load Fail :(" />', book.preview.url)
    book_preview.allow_tags = True
        
    @admin.display(ordering='is_available', boolean=True)
    def is_available(self, book):
        return book.stock > book.assigned

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct =  super().get_search_results(request, queryset, search_term)
        if 'autocomplete' in request.path:
            queryset =  queryset.filter(stock__gt=models.F('assigned'))
        return queryset, use_distinct


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = [ 'book', 'reader', 'expiry', 'do_fine', 'admin_actions']
    search_fields = [ 'book__name', 'book__isbn'  ]
    autocomplete_fields = [ 'reader', 'book' ]
    form = BorrowForm
    actions  = None
    
    def admin_actions(self, borrow):
        return format_html('<div class="admin-actions"><a class="button btn-action" href={}>Return</a></div>', reverse('admin:library-return-book', args=[borrow.pk]))
    
    def get_urls(self):
        custom_urls = [ 
                        path('admin/library/borrows/return/<int:pk>/', 
                             self.admin_site.admin_view(self.process_borrow_return),
                             name='library-return-book'
                             )
                       ]
        return custom_urls + super().get_urls();
    
    def process_borrow_return(self, request, pk):
        borrow_item = Borrow.objects.filter(pk=pk).select_related('book');
        if borrow_item.exists():
            self.message_user(request, f"{borrow_item.first().book.name} returned.", "SUCCESS")
            borrow_item.delete()
        else:
            self.message_user(request, "Item doesn't exist anymore.", "ERROR")

        return HttpResponseRedirect(reverse('admin:library_borrow_changelist'))
    
    
    @admin.display(boolean=True, ordering='expiry')
    def do_fine(self, borrow):
        return borrow.expiry > borrow.gave_time


    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        
        if db_field.name == 'book':
            kwargs['queryset'] = Book.objects.filter(stock__gt=models.F('assigned'))
        
        return super().formfield_for_foreignkey(db_field, request, *args, **kwargs)