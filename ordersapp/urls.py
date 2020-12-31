from django.urls import path
import ordersapp.views as views
from ordersapp.views import ProdctsAjaxHandler

app_name = 'orders'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='list'),
    path('create/', views.OrderCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.OrderDeleteView.as_view(), name='delete'),
    path('read/<int:pk>', views.OrderRead.as_view(), name='read'),
    path('forming_complete/<int:pk>/', views.order_forming_complete, name='forming_complete'),
    path('products_get', ProdctsAjaxHandler, name='products_ajax')
]
