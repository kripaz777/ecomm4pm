from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<slug>', ProductView.as_view(), name='detail'),
    path('subcategory/<slug>', SubCategoryProductView.as_view(), name='subcategory'),
]
