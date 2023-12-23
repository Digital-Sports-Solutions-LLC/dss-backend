from django.urls import path
from .views import TimeoutListCreateView, TimeoutRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', TimeoutListCreateView.as_view(), name='timeout_list_create'),
    path('api/<int:pk>/', TimeoutRetrieveUpdateDestroyView.as_view(), name='timeout_retrieve_update_destroy'),
]
