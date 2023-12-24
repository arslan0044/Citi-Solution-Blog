from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_on', 'slug','comments']

