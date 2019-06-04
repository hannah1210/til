from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('random_img/', views.random_img)
]