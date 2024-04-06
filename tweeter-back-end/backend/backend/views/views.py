# myapp/views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.models import Friendship, User, Post, Comment
from ..serializers.serializers import CommentCreateSerializer, PostCreateSerializer, UserSerializer, PostSerializer, CommentSerializer

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
    
class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        # serializer.save(UserID=self.request.user) - use this line of code once user authentication is implemented
        user_id = self.request.data.get('UserID')
        if user_id is not None:
            # Retrieve the User instance
            try:
                user_instance = User.objects.get(UserID=user_id)
            except User.DoesNotExist:
                # Handle case where User does not exist
                raise ValueError("User with ID {} does not exist.".format(user_id))
            # Assign the User instance to the Post
            serializer.validated_data['UserID'] = user_instance
        serializer.save()

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('UserID')
        post_id = self.request.data.get('PostID') #TODO: Make this more dynamic soon
        # Check if both user_id and post_id are present in the request data
        if user_id is not None and post_id is not None:
            try:
                # Get the User and Post objects using the provided IDs
                user = User.objects.get(UserID=user_id)
                post = Post.objects.get(PostID=post_id)
                
                # Save the comment associating it with the User and Post
                serializer.save(UserID=user, PostID=post)
            except User.DoesNotExist:
                # Handle case where User with the provided ID does not exist
                raise ValueError("User with ID {} does not exist.".format(user_id))
            except Post.DoesNotExist:
                # Handle case where Post with the provided ID does not exist
                raise ValueError("Post with ID {} does not exist.".format(post_id))
        else:
            # Handle case where UserID or PostID is missing in the request data
            raise ValueError("User and Post ID are required")
        
# TODO: Adding Likes to Posts and Comments    

class PostLikeCreateView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(PostID=post_id)
            post.LikesCount += 1
            post.save()
            return Response({"message": "Post liked successfully"}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)

class CommentLikeCreateView(APIView):
    def post(self, request, comment_id):
        try:
            comment = Comment.objects.get(CommentId=comment_id)
            comment.LikesCount += 1
            comment.save()
            return Response({"message": "Comment liked successfully"}, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({"error": "Comment does not exist"}, status=status.HTTP_404_NOT_FOUND)