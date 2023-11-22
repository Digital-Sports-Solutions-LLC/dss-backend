from django.urls import path
from . import views

urlpatterns = [
    path('', views.matches, name='matches'),
    path('create/', views.create, name='create'),
]
