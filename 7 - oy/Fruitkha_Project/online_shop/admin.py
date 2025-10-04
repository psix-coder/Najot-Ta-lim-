from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, ProductImage, Comment, News

admin.site.site_header = "Fruitkha"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk',)
    list_editable = ('name',)
    prepopulated_fields = {"slug": ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'quantity', 'price', 'weight', 'category', 'get_image')
    list_display_links = ('pk', 'name')
    list_editable = ('price', 'weight', 'quantity')
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {'slug': ('name',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            if Category.objects.all().exists():
                kwargs['empty_label'] = 'Tanlang'
            else:
                kwargs['empty_label'] = "Mavjud emas"
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "weight":
            kwargs['choices'] = db_field.get_choices(
                include_blank=True,
                blank_choice=[("", "Tanlang")]
            )
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fields = [field.name for field in Product._meta.fields if field.name != 'id']
        return [("Mahsulot", {'fields': fields})]

    def get_image(self, product):
        images = product.images.all()
        if images:
            return mark_safe(f'<img src="{images[0].image.url}" width="100px;"></img>')
        return ''

    get_image.short_description = 'Rasmi'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'created')
    list_display_links = ('pk', 'text')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'created_at', 'get_image')
    list_display_links = ('pk', 'title')

    def get_image(self, news):
        return mark_safe(f'<img src="{news.photo.url}" width="100px;"></img>')
    get_image.short_description = 'Rasmi'