from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('',views.product_list,name='product-list'),
    path('detail/<int:pk>/<slug:slug>/',views.product_detail,name='product-detail'),
    path('products-by/<slug:slug>/',views.products_by,name='products-by'),
]
