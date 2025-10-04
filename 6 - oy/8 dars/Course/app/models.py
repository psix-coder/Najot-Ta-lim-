from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    description = models.TextField(verbose_name='Tavsifi')

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE, verbose_name='Cursi')
    title = models.CharField(max_length=100, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Mazmuni')

    def __str__(self):
        return self.title
