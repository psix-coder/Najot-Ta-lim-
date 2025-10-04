from django.urls import path
from .views import home_view, animals_by_category, detail

urlpatterns = [
    path('', home_view, name='home'),
    path('animals/category/<int:category_id>/', animals_by_category, name='sort_animals'),
    path('animal/<int:animal_id>/', detail, name='detail'),
]
