from django.urls import path
from .views import User_TeamListCreateView, User_TeamRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', User_TeamListCreateView.as_view(), name='user_team_list_create'),
    path('api/<int:pk>/', User_TeamRetrieveUpdateDestroyView.as_view(), name='user_team_retrieve_update_destroy'),
]
