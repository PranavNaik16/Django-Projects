from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route to the calculator
]