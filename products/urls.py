from django.urls import path

from products import views as products_views

urlpatterns = [
    path('', products_views.index, name='products-index'),
]
