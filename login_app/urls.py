from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('register', views.register),
    path('success', views.success),
    path('check_login', views.check_login),
    path('logout', views.logout)
]
