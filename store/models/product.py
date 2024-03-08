from django.db import models
from .category import Category

# Create your models here.
  
class Product(models.Model):
  name = models.CharField(max_length = 30 )
  description= models.TextField(max_length= 200 , null= True, blank = True)
  price = models.IntegerField(default=0)
  image= models.ImageField(upload_to="Upload/Product/", null= True, blank=True)
  
  category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
  
  @staticmethod
  def get_all_products():
    return Product.objects.all()
  
  @staticmethod
  def get_all_products_by_category_id(category_id):
    if category_id:
     return Product.objects.filter(category_id=category_id)
   
    else:
      return Product.get_all_products()
  
    
 
  def __str__(self):
    return self.name 