from django.db import models
from django.core.exceptions import ValidationError  

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_year = models.IntegerField()
    photo = models.ImageField(upload_to='car_photos/', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name
