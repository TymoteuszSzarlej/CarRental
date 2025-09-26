from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_list, name='orders_list'),
    path('create/', views.create_order, name='create_order'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
]