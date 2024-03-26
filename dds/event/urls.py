from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView, addEvent
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/', EventListCreateView.as_view(), name='event_list_create'),
    path('api/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event_retrieve_update_destroy'),
    path('add-event/', addEvent, name='datatest'),
    path('andrewtest/', TemplateView.as_view(template_name='eventpage.html'), name='EventPage')
]
