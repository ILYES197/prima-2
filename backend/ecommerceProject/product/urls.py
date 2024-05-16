from django.urls import path
from . import views


urlpatterns = [
    
    path('products/', views.get_all_products, name='products'),
    path('products/<str:pk>/', views.get_by_id_product, name='get_by_id_product'),
   
    
    
    path('<str:pk>/reviews', views.create_review,name='create_review'),
    path('<str:pk>/reviews/delete', views.delete_review,name='delete_review'),
    
    
]