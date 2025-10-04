from django.contrib import admin

from .models import Courses, Students


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'image')


admin.site.register(Courses)
admin.site.register(Students)
