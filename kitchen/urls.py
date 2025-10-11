from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('' , views.kitchen_list , name = 'kitchen_list'),
    path('status/change/<int:order_id>' , views.kitchen_change_status , name = 'kitchen_change_status'),
]