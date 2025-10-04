from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Tur nomi')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL atamasi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tur '
        verbose_name_plural = 'Turlar'


WEIGHT_TYPES = {
    "kg": "kg",
    "g": "g",
    "mg": "mg",
    "l": "l",
    "ml": "ml"
}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nomi")
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL atamasi')
    description = models.TextField(max_length=1500, blank=True, null=True, default="Ma'lumot qo'shilmagan!", verbose_name="Haqida")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    weight = models.IntegerField(verbose_name="Og'irligi")
    weight_type = models.CharField(max_length=2, choices=WEIGHT_TYPES, default='kg', verbose_name="O'lchov birligi")
    quantity = models.IntegerField(default=15, verbose_name='Miqdori')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Turi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot '
        verbose_name_plural = 'Mahsulotlar'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/images', verbose_name="Rasmi")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Mahsulot nomi", related_name='images')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Rasm '
        verbose_name_plural = 'Rasmlar'


class Comment(models.Model):
    text = models.CharField(max_length=1000, verbose_name='Izoh Matni')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Izoh muallifi')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Mahsulot izohi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return f"{self.author.username}|{self.text[:20]}|{self.product.name}"

    class Meta:
        verbose_name = 'Izoh '
        verbose_name_plural = 'Izohlar'
        ordering = ['-created']


class News(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Sarlavhasi')
    text = models.TextField(max_length=2000, verbose_name="Matni")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Yangilik muallifi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    photo = models.ImageField(upload_to="news/images", verbose_name="Rasmi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik '
        verbose_name_plural = 'Yangiliklar'
