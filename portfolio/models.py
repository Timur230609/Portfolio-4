from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator    


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
class Blog(models.Model,HitCountMixin):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Blogs/images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    content = RichTextField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')
    slug = models.SlugField(unique=True, blank=True)  # Slug maydoni qo'shildi

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class ProductCategory(models.Model):
    name_en = models.CharField(max_length=250)
    name_uz = models.CharField(max_length=250)

    def __str__(self):
        from django.utils.translation import get_language
        current_language = get_language()
        if current_language == 'en':
            return self.name_en
        else:
            return self.name_uz 


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=3,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    description = RichTextField()
    sku = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/product')
    main_information = models.CharField(max_length=100)
    weight = models.FloatField()
    dimension = models.TextField()
    purchased_place = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    shipping = models.BigIntegerField()
    care_info = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
