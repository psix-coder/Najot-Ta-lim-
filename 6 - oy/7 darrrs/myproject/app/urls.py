from django.urls import path
from . import views
from .views import add_post, update_post, register

urlpatterns = [
    path('', views.course_list, name='course_list'),  
    path('courses/<int:course_id>/lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/update/', update_post, name='update_post'),
    path('auth/register/<int:lesson_id>/', register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('lessons/add/', add_post, name='add_post'),
]

