from django.urls import path

# import Views Here
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('customers/', views.customers, name='customers'),
    path('customers_profile/', views.customers_profile, name='customers_profile'),
    path('orders/', views.orders, name='orders'),

]
