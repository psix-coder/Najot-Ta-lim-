from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3'),
    path('view4/', views.view4, name='view4'),
    path('view5/', views.view5, name='view5'),
    path('view6/', views.view6, name='view6'),
    path('view7/', views.view7, name='view7'),
    path('view8/', views.view8, name='view8'),
    path('view9/', views.view9, name='view9'),
    path('view10/', views.view10, name='view10'),
]