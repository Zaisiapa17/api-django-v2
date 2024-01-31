from django.urls import path
from . import views

urlpatterns = [ 
    path('api/', views.products),
    path('api/<int:pk>/', views.product_list),
]
