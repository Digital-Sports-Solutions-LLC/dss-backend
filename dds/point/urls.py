from django.urls import path
from .views import PointListCreateView, PointRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', PointListCreateView.as_view(), name='point_list_create'),
    path('api/<int:pk>/', PointRetrieveUpdateDestroyView.as_view(), name='point_retrieve_update_destroy'),
]
