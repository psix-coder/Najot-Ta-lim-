
from django.urls import path
from .views import index, posts_by_brands, posts_by_cars

urlpatterns = [
    path('', index, name='home'),
    path('brands/<int:brand_id>/', posts_by_brands, name='brands'),
    path('car/<int:car_id>/', posts_by_cars, name='car'),
]