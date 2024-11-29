from django.contrib import admin
from . import views
from django.urls import path,include


app_name = "silentmarket"
urlpatterns = [   
    path("", views.index, name="index"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_list/<int:category_id>/', views.category_product_list, name='category_product_list'),
    

]
