from django.db import models

class Turlar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    country = models.CharField(max_length=100, verbose_name='Davlati')

    def __str__(self):
        return self.name

class Gullar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    price = models.IntegerField(verbose_name='Narxi')
    type = models.ForeignKey(Turlar, on_delete=models.CASCADE, verbose_name='Brendi')
    
    
    def __str__(self):
        return self.name