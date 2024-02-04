from rest_framework import serializers
from .models import Reaction

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'
        read_only_fields = ('id',)

