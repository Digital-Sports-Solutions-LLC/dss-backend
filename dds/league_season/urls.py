from django.urls import path
from .views import League_SeasonListCreateView, League_SeasonRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', League_SeasonListCreateView.as_view(), name='league_season_list_create'),
    path('api/<int:pk>/', League_SeasonRetrieveUpdateDestroyView.as_view(), name='league_season_retrieve_update_destroy'),
]
