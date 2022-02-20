from django.db import models
from treebeard.ns_tree import NS_Node


class Category(NS_Node):
    name            = models.CharField(max_length=255)
    node_order_by   = ['name']

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'