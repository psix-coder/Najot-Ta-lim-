from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    country = models.CharField(max_length=100, verbose_name='Davlati')

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    country = models.CharField(max_length=100, verbose_name='Davlati')
    price = models.IntegerField(verbose_name='Narxi')
    year = models.IntegerField(verbose_name='Yili')
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")
    brend = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brendi')

    def __str__(self):
        return self.name
    


