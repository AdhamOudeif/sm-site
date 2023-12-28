# views/post_view.py

from rest_framework import viewsets
from models.post_model import Post
from serializers.post_serializer import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
