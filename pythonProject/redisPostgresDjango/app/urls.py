from django.urls import path, include
from . import views

urlpatterns = [
    # path('users/', views.main, name="users")
    path('users/<int:user_id>', views.main, name="users")
]