from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
