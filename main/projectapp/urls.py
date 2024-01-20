from django.urls import path
from . import views
app_name='furniture'
urlpatterns = [
    path('',views.home,name='home'),
    path('category/',views.category,name='category'),
    path('category/<int:id>/',views.category,name='category'),
    path('details/<int:id>/',views.details,name='details')
    
]
