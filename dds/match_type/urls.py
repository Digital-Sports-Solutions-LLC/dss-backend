from django.urls import path
from .views import Match_TypeListCreateView, Match_TypeRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', Match_TypeListCreateView.as_view(), name='event_type_list_create'),
    path('api/<int:pk>/', Match_TypeRetrieveUpdateDestroyView.as_view(), name='event_type_retrieve_update_destroy'),
]
