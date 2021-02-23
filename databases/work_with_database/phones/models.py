from django.db import models
from django.urls import reverse


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=True)


    def __str__(self):
        return f"{self.id}: {self.name}"
