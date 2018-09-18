from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post

        fields = ['author', 'title', 'text', 'photo', 'created_at']