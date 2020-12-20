from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.adminview, name='view'),
    path('users/', adminapp.UsersView.as_view(), name='users'),
    path('users/<int:page>', adminapp.UsersView.as_view(), name='users'),
    path('users/personal/<int:pk>', adminapp.UsersPersonal.as_view(), name='users-personal'),
    path('users/create', adminapp.UsersCreate.as_view(), name='users-create'),
    path('users/edit/<int:pk>', adminapp.UsersEdit.as_view(), name='users-edit'),
    path('users/delete/<int:pk>', adminapp.UsersDelete.as_view(), name='users-delete'),

    path('products/', adminapp.ProdcutsView.as_view(), name='products'),
    path('products/<int:page>', adminapp.ProdcutsView.as_view(), name='products'),
    path('products/personal/<int:pk>', adminapp.ProductsPersonal.as_view(), name='products-personal'),
    path('products/create', adminapp.ProductsCreate.as_view(), name='products-create'),
    path('products/edit/<int:pk>', adminapp.ProductsEdit.as_view(), name='products-edit'),
    path('products/delete/<int:pk>', adminapp.ProductsDelete.as_view(), name='products-delete'),
]
