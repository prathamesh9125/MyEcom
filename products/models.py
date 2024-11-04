from django.db import models
from base.models import BaseModel

# Create your models here.
class Category(BaseModel):
    category_name = models.CharFile(max_lenght=100)
    category_image = models.ImageField(upload="categories")
    slug = models.SlugField(unique=True, null=True, blank= True)
    
class Product(BaseModel):
    Product_name = models.CharFile(max_lenght=100)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="prodcuts")
    price = models.IntegerField()
    Product_discription = models.TextField()
    
class ProductImage(BaseModel):
    Product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image = models.ImageField(uploads="product")
    


