
from django.urls import path
from .views import index,order_detail

urlpatterns = [
    path('',index, name='index'),
    path('order/<int:pk>',order_detail, name='order_detail'),
]
