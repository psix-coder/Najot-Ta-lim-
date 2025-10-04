from django.contrib import admin
from .models import FoodType, Foods, Comment


@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk',)
    list_editable = ('name',)
    list_filter = ('name',) 
    search_fields = ('name',)  
    actions_on_top = False
    actions_on_bottom = True


@admin.register(Foods)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'food_type')
    list_display_links = ('pk',)
    list_editable = ('name', 'price')
    list_filter = ('food_type', 'price')  
    search_fields = ('name', 'food_type__name')  
    actions_on_top = False
    actions_on_bottom = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'food', 'author', 'created')
    list_display_links = ('pk', 'text')
    list_filter = ('food', 'author', 'created')  
    search_fields = ('text', 'food__name', 'author__username')  
    date_hierarchy = 'created'  
    actions_on_top = False
    actions_on_bottom = True