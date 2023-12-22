from django.urls import path
from .views import TeamListCreateView, TeamRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', TeamListCreateView.as_view(), name='team_list_create'),
    path('api/<int:pk>/', TeamRetrieveUpdateDestroyView.as_view(), name='team_retrieve_update_destroy'),
]
