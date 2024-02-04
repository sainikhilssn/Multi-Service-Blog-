from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','title','content')
        read_only_fields = ('id',)