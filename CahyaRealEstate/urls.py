from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('populate/', views.populate_properties, name='populate_properties'),
]
