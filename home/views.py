from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
# def home(request):

# 	return render(request,'index.html')

class BaseView(View):
	views = {}

class HomeView(BaseView):
	def get(self,request):
		self.views['products'] = Product.objects.all()
		self.views['hots'] = Product.objects.filter(labels = 'hot')
		self.views['categories'] = Category.objects.all()
		self.views['sliders'] = Slider.objects.all()
		return render(request,'index.html',self.views)