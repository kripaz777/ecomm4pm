from django.shortcuts import render,redirect
from django.views.generic import View
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
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


def signup(request):
	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request,"This username is already taken")
				return redirect('/signup')

			elif User.objects.filter(email = email).exists():
				messages.error(request,"This email is already taken")
				return redirect('/signup')

			else:
				data = User.objects.create_user(
					first_name = first_name,
					last_name = last_name,
					username = username,
					email = email,
					password = password
					)
				
				data.save()

				messages.success(request,"You are registered")
				return redirect('/signup')

		else:
			messages.success(request,"Password does not match")
			return redirect('/signup')

	return render(request,'register.html')


