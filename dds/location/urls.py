from django.urls import path
from .views import LocationListCreateView, LocationRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', LocationListCreateView.as_view(), name='location_list_create'),
    path('api/<int:pk>/', LocationRetrieveUpdateDestroyView.as_view(), name='location_retrieve_update_destroy'),
]
