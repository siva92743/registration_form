from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_register', views.user_register, name='user_register'),
    path('user_panel', views.user_panel, name='user_panel'),
    path('login_view', views.login_view, name='login_view'),
]
