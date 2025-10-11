from django.urls import path
from . import views
app_name = 'delivery'

urlpatterns = [
    path('list/' , views.delivery_list , name='delivery_list'),
    path('status/change/<int:order_id>' , views.change_delivery_status , name='change_delivery_status'),
]