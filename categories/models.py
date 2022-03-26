from django.db import models
from treebeard.ns_tree import NS_Node
from .managers import CategoryManager


class Category(NS_Node):
    name            = models.CharField(max_length=255)
    node_order_by   = ['name']

    def natural_key(self):
        return [ self.name, self.depth ]

    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'