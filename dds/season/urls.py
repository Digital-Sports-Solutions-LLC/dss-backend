from django.urls import path
from .views import SeasonListCreateView, SeasonRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', SeasonListCreateView.as_view(), name='season_list_create'),
    path('<int:pk>/api/', SeasonRetrieveUpdateDestroyView.as_view(), name='season_retrieve_update_destroy'),
]
