from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loop/', views.loop, name='loop'),
    path('dashboard/', views.dashboard, name='dashboard')
]