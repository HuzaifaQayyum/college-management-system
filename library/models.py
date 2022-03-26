from django.db import models
from django.conf import settings

from .managers import AuthorManager, BookManager


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    objects = AuthorManager()

    def natural_key(self):
        return [ self.name ]

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    isbn            = models.CharField(max_length=13, unique=True)
    category        = models.ForeignKey(settings.CATEGORY_MODEL, on_delete=models.PROTECT)
    name           = models.CharField(max_length=200, db_index=True)
    preview         = models.ImageField(upload_to='images/books/')
    author          = models.ManyToManyField(Author, db_index=True)
    stock           = models.PositiveIntegerField(default=0)
    assigned        = models.PositiveIntegerField(default=0, editable=False)
    
    objects = BookManager()

    def natural_key(self):
        return [ self.isbn ]

    def __str__(self) -> str:
        return self.name


class Borrow(models.Model):
    reader           = models.ForeignKey(settings.BORROWER_MODEL, on_delete=models.PROTECT)
    book             = models.ForeignKey(Book, on_delete=models.PROTECT)
    gave_time        = models.DateField(auto_now_add=True)
    expiry           = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.reader} - {self.book}"
    
    class Meta:
        permissions = [ ('can_return_book', 'Can return books')]