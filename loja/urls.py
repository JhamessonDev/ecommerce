from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('loja/', views.loja, name='loja'),
    path('minhaconta/', views.minha_conta, name='minha_conta'),
    path('login/', views.login, name='login'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('checkout/', views.checkout, name='checkout'),
]
