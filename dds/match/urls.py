from django.urls import path
from .views import MatchListCreateView, MatchRetrieveUpdateDestroyView, match

urlpatterns = [
    path('api/', MatchListCreateView.as_view(), name='match_list_create'),
    path('api/<int:pk>/', MatchRetrieveUpdateDestroyView.as_view(), name='match_retrieve_update_destroy'),
    path('test/', match, name='match_test'),
]
