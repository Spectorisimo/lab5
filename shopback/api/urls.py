from django.urls import path
from .views import ProductsListAPI, ProductsRetrieveAPI, CategoriesListAPI, CategoriesRetrieveAPI, CategoryProductsListAPI

urlpatterns = [
    path('products/', ProductsListAPI.as_view()),
    path('products/<int:pk>/', ProductsRetrieveAPI.as_view()),
    path('categories/', CategoriesListAPI.as_view()),
    path('categories/<int:pk>/', CategoriesRetrieveAPI.as_view()),
    path('categories/<int:pk>/products/', CategoryProductsListAPI.as_view()),
]
