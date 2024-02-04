from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','blogId', 'text')
        read_only_fields = ('id',)