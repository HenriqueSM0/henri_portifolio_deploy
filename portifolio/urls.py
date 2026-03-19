from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.proj_list, name='projetos'),
    path('email/', views.email, name='email'),
]