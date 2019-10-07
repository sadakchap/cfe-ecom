from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name    = models.CharField(max_length=255)
    slug    = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('product:product_by',kwargs={'slug':self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name    = models.CharField(max_length=255,db_index=True)
    slug    = models.SlugField(max_length=255,db_index=True,unique=True)
    brand   = models.CharField(max_length=255)
    desc    = models.TextField()
    image   = models.ImageField(upload_to='uploads/%Y/%m/%d/',blank=True,null=True)
    price   = models.DecimalField(max_digits=10,decimal_places=2)
    stock   = models.PositiveIntegerField(default=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # available = models.BooleanField(default=True)

    @property
    def available(self):
        return self.stock>0

    class Meta:
        index_together = (('id','slug'),)
        ordering = ('-created',)
        # available.boolean = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:detail',kwargs={'pk':self.pk,'slug':self.slug})
