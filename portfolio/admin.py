from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register((Contact,Category,Blog,Product,ProductCategory)) 