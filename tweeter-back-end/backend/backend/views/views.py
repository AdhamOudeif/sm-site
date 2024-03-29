# myapp/views.py

from rest_framework import generics
from ..models.models import Friendship, User, Post, Comment
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
    
class FriendsPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        friends_ids = Friendship.objects.filter(User1ID=user_id, Status='Accepted').values_list('User2ID', flat=True)
        friends_posts = Post.objects.filter(UserID__in=friends_ids)
        return friends_posts
