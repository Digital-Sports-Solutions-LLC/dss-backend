from django.urls import path
from .views import LeagueListCreateView, LeagueRetrieveUpdateDestroyView

urlpatterns = [
    path('league/', LeagueListCreateView.as_view(), name='league_list_create'),
    path('league/<int:pk>/', LeagueRetrieveUpdateDestroyView.as_view(), name='league_retrieve_update_destroy'),
]
