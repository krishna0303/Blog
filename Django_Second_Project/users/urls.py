from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='blog-register'),
    path('about/', views.about, name='blog-login'),

]
