from django.urls import path
from .views import CourtListCreateView, CourtRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', CourtListCreateView.as_view(), name='court_list_create'),
    path('api/<int:pk>/', CourtRetrieveUpdateDestroyView.as_view(), name='court_retrieve_update_destroy'),
]
