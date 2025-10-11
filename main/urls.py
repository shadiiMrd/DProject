from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('qr/', views.cafe_qr, name='cafe_qr'),
]