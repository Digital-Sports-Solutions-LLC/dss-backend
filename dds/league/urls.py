from django.urls import path
from .views import LeagueListCreateView, LeagueRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', LeagueListCreateView.as_view(), name='league_list_create'),
    path('<int:pk>/api/', LeagueRetrieveUpdateDestroyView.as_view(), name='league_retrieve_update_destroy'),
]
