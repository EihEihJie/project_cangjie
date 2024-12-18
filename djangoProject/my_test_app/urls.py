from django.urls import path
from my_test_app import views

urlpatterns = [
    path('index/', views.index),
]