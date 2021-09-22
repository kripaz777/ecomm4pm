from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse
from .models import *
# Create your views here.
# def home(request):

# 	return render(request,'index.html')

class BaseView(View):
	views = {}
	views['categories'] = Category.objects.all()
	views['subcategories'] = SubCategory.objects.all()

class HomeView(BaseView):
	def get(self,request):
		self.views['products'] = Product.objects.all()
		self.views['hots'] = Product.objects.filter(labels = 'hot')
		self.views['categories'] = Category.objects.all()
		self.views['sliders'] = Slider.objects.all()
		return render(request,'index.html',self.views)


class ProductView(BaseView):
	def get(self,request,slug):
		self.views['product_detail'] = Product.objects.filter(slug = slug)
		return render(request,'single.html',self.views)

class SubCategoryProductView(BaseView):
	def get(self,request,slug):
		ids = SubCategory.objects.get(slug = slug).id
		self.views['subcategory_product'] = Product.objects.filter(subcategory_id = ids)
		return render(request,'kitchen.html',self.views)

