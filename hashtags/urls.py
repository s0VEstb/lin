from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_clothes, name='all'),
    path('older/', views.older_list, name='older'),
    path('younger/', views.younger_list, name='younger'),
    path('kids/', views.kids_list, name='kids'),  
]
