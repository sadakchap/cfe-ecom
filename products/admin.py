from django.contrib import admin
from .models import Product,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','brand','price','stock','created','available',)
    list_filter  = ('brand','category',)
    prepopulated_fields = {'slug':('name','brand',)}

admin.site.register(Product,ProductAdmin)
