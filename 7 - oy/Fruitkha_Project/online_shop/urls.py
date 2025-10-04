from django.urls import path
from django.views.generic import TemplateView
from .views import (HomeListView, ProductDetail, cart, NewsListView, contact, ShopListView, check_out,
                    NewsDetailView)

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html', extra_context={'title': "About"}), name='about'),
    path('contact/', contact, name='contact'),

    # shop
    path('shop/', ShopListView.as_view(), name='shop'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', check_out, name='checkout'),

    # news
    path('news/', NewsListView.as_view(), name='news'),
    path('new/<int:news_id>/detail/', NewsDetailView.as_view(), name='news_detail'),
]
