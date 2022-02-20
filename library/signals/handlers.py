from django.db.models.signals import post_delete
from django.dispatch import receiver
from library.models import Book, Borrow
from django.db.models.expressions import F

@receiver(post_delete, sender=Borrow)
def on_delete_borrow(sender, instance, **kwargs):
    Book.objects.filter(pk=instance.book.pk).update(assigned=F('assigned') - 1)