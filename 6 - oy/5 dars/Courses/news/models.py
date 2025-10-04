from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=100, verbose_name="Kurs nomi")
    descriptions = models.TextField(verbose_name="Kurs tavsifi")
    image = models.ImageField(upload_to='course_images/', verbose_name="Kurs rasmi", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(max_length=100, verbose_name="Talaba ismi")
    email = models.EmailField(max_length=100, unique=True)
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="students", verbose_name="Kurs")
    
    def __str__(self):
        return self.name

