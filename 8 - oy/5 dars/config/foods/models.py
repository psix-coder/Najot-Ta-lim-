from django.db import models


class Foods(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ovqat'
        verbose_name_plural = 'Ovqatlar'


class FoodType(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nomi")
    composition = models.TextField(verbose_name="Tarkibi")
    price = models.PositiveIntegerField(verbose_name="Narxi")
    food = models.ForeignKey(
        Foods, 
        on_delete=models.CASCADE, 
        related_name='food_types', 
        verbose_name="Ovqat"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ovqat turi'
        verbose_name_plural = 'Ovqat turlari'


class Comment(models.Model):
    text = models.TextField(verbose_name="Matn")
    food = models.ForeignKey(
        Foods, 
        on_delete=models.CASCADE, 
        related_name='comments', 
        verbose_name="Ovqat"
    )
    author = models.CharField(max_length=150, verbose_name="Muallif")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"Izoh #{self.pk} - {self.food.name}"

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'
        ordering = ['-created']