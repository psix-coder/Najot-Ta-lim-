import random

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Category, Product, ProductImage, Comment, News


class HomeListView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    extra_context = {
        'title': 'Fruitkha | Main Page'
    }

    def get_queryset(self):
        products = Product.objects.order_by('?')[:3]
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['news'] = News.objects.order_by('?')[:3]
        return context


class ShopListView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    extra_context = {
        'title': "Shop"
    }

    def get_queryset(self):
        products = Product.objects.order_by('?')[:6]
        length_products = len(products)
        products_list = []
        i = 0
        while i <= length_products:
            product_index = random.randint(0, length_products - 1)
            product = products[product_index]
            if product not in products_list:
                products_list.append(product)
            if len(products_list) >= 10:
                break
            i += 1
        return products_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'single-product.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product'] = Product.objects.get(slug=self.kwargs.get('slug'))
        context['title'] = f'{self.object.name}: {self.object.description}'
        return context


class NewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    extra_context = {
        'title': "News"
    }


class NewsDetailView(DetailView):
    model = News
    template_name = 'single-news.html'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new'] = self.object
        context['news'] = News.objects.all()
        context['title'] = f"{self.object.title}"
        return context


def cart(request):
    context = {
        'title': 'Cart'
    }
    return render(request, 'cart.html', context)


def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'contact.html', context)


def check_out(request):
    context = {
        'title': 'Checkout'
    }
    return render(request, 'checkout.html', context)
