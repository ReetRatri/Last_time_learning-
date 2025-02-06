from django.urls import path
from . import views
from .views import *


urlpatterns = [
    # path('', views.item_list, name='item_list'),
    # path('index/', views.index),
    path('books/', views.book_list, name='book_list'),
    
    ]