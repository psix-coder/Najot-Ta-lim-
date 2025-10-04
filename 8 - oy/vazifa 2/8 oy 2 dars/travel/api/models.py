# from django.db import models
#
#
# class Klass(models.Model):
#     name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
#     price = models.IntegerField(verbose_name="Narxi")
#
#     def __str__(self):
#         return self.name
#
#
# class Hotel(models.Model):
#     name = models.CharField(max_length=150, verbose_name="Nomi")
#     stars = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Yulduzlar soni")
#     price = models.IntegerField(verbose_name="Narxi")
#
#     def __str__(self):
#         return f"{self.name} ({self.stars}⭐) - {self.price} so'm"


# class Travel(models.Model):
#     name = models.CharField(max_length=150, unique=True, verbose_name="Nomi")
#     comment = models.TextField(verbose_name="Izoh")
#     term = models.DateTimeField(auto_now_add=True, verbose_name="Muddati")
#     price = models.IntegerField(verbose_name="Narxi")
#     klass = models.ForeignKey(Klass, on_delete=models.CASCADE, verbose_name="Klass")
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="travels", verbose_name="Mehmonxona")

#     # def save(self, *args, **kwargs):
#     #     if not self.term:
#     #         self.term = now() + timedelta(days=7)
#     #     super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name
