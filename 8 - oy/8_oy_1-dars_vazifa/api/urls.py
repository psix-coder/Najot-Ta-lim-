from django.urls import path
from .views import HomeView, GenreView

urlpatterns = [
    path('books/', HomeView.as_view()),
    path('books/<int:pk>/', HomeView.as_view()),
    path('genres/', GenreView.as_view()),
    path('genres/<int:pk>', GenreView.as_view()),
]
