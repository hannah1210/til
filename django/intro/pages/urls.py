from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('hola/',views.hola),
    path('dinner/',views.dinner),
    path('hello/<str:name>/',views.hello),
    path('introduce/<name>/<int:age>', views.introduce),
    path('times/<int:num1>/<int:num2>', views.times),
    path('circle/<int:r>', views.circle),
    path('template_language/',views.template_language),
    path('birthday/', views.birthday),
    path('throw/',views.throw),
    path('catch/',views.catch),
    path('lotto/', views.lotto),
    path('get/', views.get)
]