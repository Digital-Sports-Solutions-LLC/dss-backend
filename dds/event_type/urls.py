from django.urls import path
from .views import Event_TypeListCreateView, Event_TypeRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', Event_TypeListCreateView.as_view(), name='event_type_list_create'),
    path('api/<int:pk>/', Event_TypeRetrieveUpdateDestroyView.as_view(), name='event_type_retrieve_update_destroy'),
]
