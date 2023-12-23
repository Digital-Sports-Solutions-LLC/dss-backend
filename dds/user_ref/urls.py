from django.urls import path
from .views import User_RefListCreateView, User_RefRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', User_RefListCreateView.as_view(), name='user_ref_list_create'),
    path('api/<int:pk>/', User_RefRetrieveUpdateDestroyView.as_view(), name='user_ref_retrieve_update_destroy'),
]
