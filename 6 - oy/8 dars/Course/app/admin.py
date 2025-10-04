from django.contrib import admin
from .models import Course, Lesson


class Course_Admin(admin.ModelAdmin):
    list_display = ('name', 'descriptions')

admin.site.register(Course)


class Lesson_displayh(admin.ModelAdmin):
    list_display = ('name', 'price', 'course_l')

admin.site.register(Lesson)