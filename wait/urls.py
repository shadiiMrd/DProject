from django.urls import path
from . import views

app_name = 'wait'

urlpatterns = [
    path('list/', views.wait_list, name='wait_list'),
    path('add/', views.wait_add, name='wait_add'),
    path('status/change/<int:wait_id>', views.wait_change_status, name='wait_change_status'),
]
