from django.urls import path
from . import views

urlpatterns = [
    path('demo1/', views.demo1, name='demos-demo1'),
    path('', views.home, name='demos-home'),
]
