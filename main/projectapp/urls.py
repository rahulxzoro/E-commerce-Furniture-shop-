from django.urls import path
from . import views
app_name='furniture'
urlpatterns = [
    path('',views.home,name='home'),
    path('category/',views.category,name='category'),
    path('category/<int:id>/',views.category,name='category'),
    path('details/<int:id>/',views.details,name='details'),
    path('consult/',views.consult,name='consult'),
    path('profile/',views.profile,name='profile'),
    path('address/',views.address,name='address'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('store/',views.store,name='store'),
    
    
    
]
