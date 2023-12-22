from django.urls import path
from .views import RoleListCreateView, RoleRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', RoleListCreateView.as_view(), name='role_list_create'),
    path('api/<int:pk>/', RoleRetrieveUpdateDestroyView.as_view(), name='role_retrieve_update_destroy'),
]
