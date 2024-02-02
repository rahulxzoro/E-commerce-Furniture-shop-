from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('cart/<int:id>/',views.cart,name='cart'),
    path('display/', views.display, name='display'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('dele/<int:id>/', views.dele, name='dele'),
    path('buy/',views.buy,name='buy'),
    path('order_details/<int:id>/', views.order_details, name='order_details'),

]
