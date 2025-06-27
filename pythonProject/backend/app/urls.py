from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_api, name="products"),
    path('users/', views.user_api, name="products"),
]