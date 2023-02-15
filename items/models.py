from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name} {self.price} {self.currency}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ('-id', )

    def get_absolute_url(self):
        return reverse(
            'item_detail',
            args=[str(self.id)]
        )
