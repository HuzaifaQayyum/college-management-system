from django.db import models


class AuthorManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)

class BookManager(models.Manager):

    def get_by_natural_key(self, isbn):
        return self.get(isbn=isbn)