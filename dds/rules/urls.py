from django.urls import path
from .views import RulesListCreateView, RulesRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', RulesListCreateView.as_view(), name='rules_list_create'),
    path('api/<int:pk>/', RulesRetrieveUpdateDestroyView.as_view(), name='rules_retrieve_update_destroy'),
]
