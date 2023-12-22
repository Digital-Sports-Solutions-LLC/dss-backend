from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', EventListCreateView.as_view(), name='event_list_create'),
    path('api/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event_retrieve_update_destroy'),
]
