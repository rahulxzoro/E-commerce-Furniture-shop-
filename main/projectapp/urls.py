from django.urls import path
from . import views
app_name='furniture'
urlpatterns = [
    path('',views.home,name='home')
]
