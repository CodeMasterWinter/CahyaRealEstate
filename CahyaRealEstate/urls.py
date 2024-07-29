from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('populate/', views.populate_properties, name='populate_properties'),
]
