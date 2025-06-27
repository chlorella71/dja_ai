from django.urls import path
from . import views

urlpatterns = [
    path("app/", views.main, name="app"),
]