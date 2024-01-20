from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 path('login/', views.user_login, name='login'),
 path('logout/', views.user_logout, name='logout'),
 path('register/', views.register, name='register'),
 path('', views.dashboard, name='dashboard'),
 path('password-change/', views.change_password, name='change_password'),
 path('password-change/done/', views.change_password, name='change_password_done'),
 path('edit/', views.edit, name='edit'),
 path('password-reset/', views.CustomPasswordResetView.as_view(),name='password_reset'),
 path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
 path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
 path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

