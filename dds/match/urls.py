from django.urls import path
from .views import MatchListCreateView, MatchRetrieveUpdateDestroyView, index, match, shotClocker, referee, update, spectator, summary

urlpatterns = [
    path('api/', MatchListCreateView.as_view(), name='match_list_create'),
    path('api/<int:pk>/', MatchRetrieveUpdateDestroyView.as_view(), name='match_retrieve_update_destroy'),
    path('', index, name='home'),
    path('<int:pk>', match, name='match'),
    path('<int:pk>/SC/<int:num>', shotClocker, name='shotClocker'),
    path('<int:pk>/REF', referee, name='referee'),
    path('<int:pk>/spectator', spectator, name='spectator'),
    path('<int:pk>/update', update, name='update'),
    path('<int:pk>/summary', summary, name='summary'),
]
