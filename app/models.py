from random import choices
from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS = (
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )
    item = models.CharField(max_length=400)
    status = models.CharField(choices=STATUS, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")

    def __str__(self):
        return self.item
