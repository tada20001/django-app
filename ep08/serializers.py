from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post

class PostSerializer(ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['author_username', 'message']
