from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('car_detail/<int:car_id>/', views.car_detail, name='car_detail'),
]