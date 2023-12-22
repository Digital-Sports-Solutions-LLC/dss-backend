from django.urls import path
from .views import MatchListCreateView, MatchRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', MatchListCreateView.as_view(), name='match_list_create'),
    path('<int:pk>/api/', MatchRetrieveUpdateDestroyView.as_view(), name='match_retrieve_update_destroy'),
]
