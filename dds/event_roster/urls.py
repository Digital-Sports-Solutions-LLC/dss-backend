from django.urls import path
from .views import Event_RosterListCreateView, Event_RosterRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', Event_RosterListCreateView.as_view(), name='event_roster_list_create'),
    path('api/<int:pk>/', Event_RosterRetrieveUpdateDestroyView.as_view(), name='event_roster_retrieve_update_destroy'),
]
