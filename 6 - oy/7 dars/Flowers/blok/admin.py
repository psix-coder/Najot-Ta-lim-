from django.contrib import admin
from .models import Turlar, Gullar


class Turlar_Admin(admin.ModelAdmin):
    list_display = ('name', 'country')

admin.site.register(Gullar)

class Gullar_Admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'number')
admin.site.register(Turlar)