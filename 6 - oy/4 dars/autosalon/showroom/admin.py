from django.contrib import admin
from .models import Brand, Car
from django.utils.safestring import mark_safe

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')  


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'price', 'release_year', 'photo')


    def brand_name(self, obj):
        return obj.brand.name


    def display_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="100" />')  # Assuming 'photo' is the field for the image
    display_photo.short_description = 'Photo'

