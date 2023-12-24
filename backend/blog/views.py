from rest_framework import viewsets,generics
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer