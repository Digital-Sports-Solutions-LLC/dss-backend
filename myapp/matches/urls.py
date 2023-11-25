from django.urls import path, include
from .models import Match
from rest_framework import routers, serializers, viewsets
from . import views

# Serializers define the API representation.
class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ['matchid', 'team1', 'team2', 'team1Score', 'team2Score', 'tournament', 'court', 'datetime', 'status', 'livestreamLink', 'refereeCode', 'style']
      
# ViewSets define the view behavior.
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all().values()
    serializer_class = MatchSerializer
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()  
router.register(r'', MatchViewSet)  

urlpatterns = [
    path('', views.matches, name='matches'),
    path('create/', views.create, name='create'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]