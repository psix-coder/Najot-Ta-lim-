from django.contrib import admin
from .models import Brand, Car

class Avtosalon_Admin(admin.ModelAdmin):
    list_display = ('name', 'country')

admin.site.register(Brand)

class Car_Admin(admin.ModelAdmin):
    list_display = ('name', 'country', 'price', 'year', 'brend')

admin.site.register(Car)
