from rest_framework import serializers
from .models import LEAGUE

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LEAGUE
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Check if 'graphic' is None and set it to a default value if it is
        if representation['graphic'] is None:
            request = self.context.get('request')
            if request is not None:
                domain = request.get_host()
                representation['graphic'] = f"http://{domain}/media/images/file-not-found.jpg"

            
        # Check if 'altGraphic' is None and set it to a default value if it is
        if representation['altGraphic'] is None:
            request = self.context.get('request')
            if request is not None:
                domain = request.get_host()
                representation['altGraphic'] = f"http://{domain}/media/images/file-not-found.jpg"

        return representation
