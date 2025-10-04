from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'janr '
        verbose_name_plural = 'janrlar'


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    about = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    page = models.IntegerField(default=50)
    published = models.DateTimeField(auto_now=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'kitob '
        verbose_name_plural = 'kitoblar'
