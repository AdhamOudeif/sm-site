# myapp/views.py

from rest_framework import generics
from ..models.models import User, Post, Comment
from ..serializers.serializers import UserSerializer, PostSerializer, CommentSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListByPostID(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(PostID=post_id)
