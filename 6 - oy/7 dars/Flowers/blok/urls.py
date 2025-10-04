
from django.urls import path
from . import views
from .views import add_post, update_post

urlpatterns = [
    path('', views.posts_by_gullar, name='posts_by_gullar'),
    path('gullar/<int:gullar_id>/', views.posts_by_gullar, name='posts_by_gullar'),
    path('gullar/<int:gullar_id>/', views.posts_by_gullar, name='posts_by_gullar'),
    path('gullar/<int:gullar_id>/update/', update_post, name='update_post'),
    path('gullar/blok/', add_post, name='add_post'),

]
