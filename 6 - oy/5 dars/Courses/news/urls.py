from django.urls import path

from .views import index, posts_by_courses, posts_by_students


urlpatterns = [
    path('', index, name='home'),
    path('courses/<int:course_id>/', posts_by_courses, name='courses'),
    path('student/<int:student_id>/', posts_by_students, name='students'),
]