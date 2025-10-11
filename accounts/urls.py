from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/profile/', views.edit_profile, name='edit_profile'),

    path('reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
]
