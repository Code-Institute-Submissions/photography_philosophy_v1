from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products_admin_hub/', views.products_admin_hub, name='products_admin_hub'),
    path('add_product/', views.add_product, name='add_product'),
]
