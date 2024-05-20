from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search/', views.search_listings, name='search_listings'),
    path('populate/', views.populate_properties, name='populate_properties'),
    path('suggest_locations/', views.suggest_locations, name='suggest_locations'),
]
