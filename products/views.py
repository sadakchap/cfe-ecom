from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Product,Category
from cart.models import Order
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]
    categories = Category.objects.all()[:5]
    return render(request,'products/product_list.html',{'products':products,
                                                    'categories':categories,
                                                    'current_order_products':current_order_products})

def product_detail(req,pk,slug):
    product = get_object_or_404(Product,pk=pk,slug=slug)
    return render(req,"products/product_detail.html",{'product':product})

def products_by(req,slug):
    category = get_object_or_404(Category,slug=slug)
    categories = Category.objects.all()[:5]
    products = Product.objects.filter(category=category)
    return render(req,'products/shorted_product_list.html',{'category':category,'products':products,'categories':categories})
