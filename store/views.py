from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.
def home(request):
  
  products = None
  categories = Category.get_all_categories()
  categoryID=request.GET.get('category')
  if categoryID:
    products=Product.get_all_products_by_category_id(categoryID)
  else:
    products=Product.get_all_products()
  data={}
  
  data['products']=products
  data['categories']=categories
  # return render(request, 'orders/order.html')
  return render(request, 'index.html' ,data)

def Signup(request):
  return render(request, 'signup.html')