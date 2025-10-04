from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions

from .models import Category, Product, Order  #Model qismidan modellar import qilindi
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer   # Serializers qismidan serializderlar imort qilindi





class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
