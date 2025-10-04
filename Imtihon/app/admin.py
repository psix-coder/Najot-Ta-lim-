from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import TypeCourse, Course, Lesson, LessonVideo, Comment, Teacher, Rating


@admin.register(TypeCourse, Course, Comment, Rating)
class DefaultAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course',)
    search_fields = ('title',)
    ordering = ('order',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Teacher').exists():
            return qs.filter(course__teacher__user=request.user)
        return qs

    def has_change_permission(self, request, obj=None):
        if obj and request.user.groups.filter(name='Teacher').exists():
            return obj.course.teacher.user == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='Teacher').exists():
            return False
        return True


@admin.register(LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'video_url')
    search_fields = ('lesson__title',)


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('id',)
    readonly_fields = ('last_login', 'date_joined')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ("is_superuser", "groups", "user_permissions") + self.readonly_fields
        return self.readonly_fields


admin.site.unregister(Group)
