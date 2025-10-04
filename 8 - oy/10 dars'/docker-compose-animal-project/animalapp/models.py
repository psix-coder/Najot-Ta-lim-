from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Tur "
        verbose_name_plural = "Turlar"

    def __str__(self):
        return self.name


class Animal(models.Model):
    objects = None
    name = models.CharField(max_length=150, unique=True)
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Hayvon "
        verbose_name_plural = "Hayvonlar"

    def __str__(self):
        return f"{self.category}: {self.name}"
