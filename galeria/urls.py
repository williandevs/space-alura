from django.urls import path 
from galeria.views import index  # Importe a função de visualização do seu aplicativo

urlpatterns = [
    path('', index),   # Associe a função de visualização à URL vazia
    
]
