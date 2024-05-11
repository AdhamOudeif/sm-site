# myapp/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.models import Friendship, User, Post, Comment
from ..serializers.serializers import CommentCreateSerializer, FriendRequestSerializer, PostCreateSerializer, UserCreateSerializer, UserLoginSerializer, UserSerializer, PostSerializer, CommentSerializer
from django.contrib.auth.hashers import check_password

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
        
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()  # Django's built-in authentication system will hash the password automatically

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve username/email and password from the request
        username_or_email = serializer.validated_data.get('username_or_email')
        password = serializer.validated_data.get('password')

        # Check if the username/email exists
        try:
            user = User.objects.get(Username=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(Email=username_or_email)
            except User.DoesNotExist:
                return Response({"error": "Invalid username/email or password"}, status=status.HTTP_400_BAD_REQUEST)

        # Verify password
        if check_password(password, user.Password):
            # Password is correct, user authenticated
            return Response({"message": "User authenticated successfully"}, status=status.HTTP_200_OK)
        else:
            # Password is incorrect
            return Response({"error": "Invalid username/email or password"}, status=status.HTTP_400_BAD_REQUEST)
        
class SendFriendRequestCreateView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer

    def create(self, request, *args, **kwargs):
        # Extract user IDs from the request data
        user1_id = self.request.data.get('User1ID')
        user2_id = self.request.data.get('User2ID')
        # Ensure that user1_id is smaller than user2_id
        if user1_id > user2_id:
            user1_id, user2_id = user2_id, user1_id

        # Convert user IDs to User instances
        user1 = User.objects.get(pk=user1_id)
        user2 = User.objects.get(pk=user2_id)

        # Check if any friendship already exists with the specified users and status
        if Friendship.objects.filter(User1ID=user1, User2ID=user2).exists():
            friendship = Friendship.objects.get(User1ID=user1, User2ID=user2)
            friendshipStatus = friendship.Status
            
            # Switch-like logic for different status cases
            if friendshipStatus.lower() == 'pending':
                return Response({"error": "Pending friendship already exists"}, status=status.HTTP_400_BAD_REQUEST)
            elif friendshipStatus.lower() == 'accepted':
                return Response({"error": "Accepted friendship already exists"}, status=status.HTTP_400_BAD_REQUEST)
            elif friendshipStatus.lower() == 'rejected':
                return Response({"error": "Declined friendship already exists"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Handle other status cases if needed
                pass

        # Create a friendship entry with status='pending'
        Friendship.objects.create(User1ID=user1, User2ID=user2, Status='pending')

        return Response({"message": "Friend request sent successfully"}, status=status.HTTP_201_CREATED)
    
class AcceptFriendRequestView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer

    def update(self, request, *args, **kwargs):
        user1_id = self.request.data.get('User1ID')
        user2_id = self.request.data.get('User2ID')
        # Ensure that user1_id is smaller than user2_id
        if user1_id > user2_id:
            user1_id, user2_id = user2_id, user1_id

        # Convert user IDs to User instances
        user1 = User.objects.get(pk=user1_id)
        user2 = User.objects.get(pk=user2_id)
        # Retrieve the specific friendship instance
        friendship = Friendship.objects.get(User1ID=user1, User2ID=user2)

        # Retrieve the specific friendship instance or return 404 if not found
        friendship = get_object_or_404(Friendship, User1ID=user1, User2ID=user2)

        # Check if the friendship status is pending before accepting it
        if friendship.Status.lower() != 'pending':
            return Response({"error": "Friend request is not pending"}, status=status.HTTP_400_BAD_REQUEST)


        # Update the status of the friendship to 'accepted'
        friendship.Status = 'accepted'
        friendship.save()
        return Response({"message": "Friend request accepted successfully"}, status=status.HTTP_200_OK)

class RejectFriendRequestView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer

    def update(self, request, *args, **kwargs):
        user1_id = self.request.data.get('User1ID')
        user2_id = self.request.data.get('User2ID')
        # Ensure that user1_id is smaller than user2_id
        if user1_id > user2_id:
            user1_id, user2_id = user2_id, user1_id

        # Convert user IDs to User instances
        user1 = User.objects.get(pk=user1_id)
        user2 = User.objects.get(pk=user2_id)
        # Retrieve the specific friendship instance
        friendship = Friendship.objects.get(User1ID=user1, User2ID=user2)

        # Retrieve the specific friendship instance or return 404 if not found
        friendship = get_object_or_404(Friendship, User1ID=user1, User2ID=user2)

        # Check if the friendship status is pending before accepting it
        if friendship.Status.lower() != 'pending':
            return Response({"error": "Friend request is not pending"}, status=status.HTTP_400_BAD_REQUEST)


        # Update the status of the friendship to 'accepted'
        friendship.Status = 'rejected'
        friendship.save()
        return Response({"message": "Friend request rejected successfully"}, status=status.HTTP_200_OK)
    
class FriendRequestListView(generics.ListAPIView):
    serializer_class = UserSerializer  # Assuming you have a serializer for the User model

    def get_queryset(self):
        # Retrieve the user ID from the URL parameters
        user_id = self.kwargs.get('user_id')

        # Filter the queryset to retrieve all pending friendship requests where User1ID=user_id
        queryset = Friendship.objects.filter(User1ID=user_id, Status='pending')

        # Extract a list of UserID2 from the queryset
        user_ids = queryset.values_list('User2ID', flat=True)

        # Retrieve the corresponding User objects
        users = User.objects.filter(pk__in=user_ids)

        return users

    def list(self, request, *args, **kwargs):
        # Get the list of User objects who sent friend requests
        users = self.get_queryset()

        # Serialize the User objects
        serializer = self.get_serializer(users, many=True)

        # Return the serialized User objects as JSON response
        return JsonResponse(serializer.data, safe=False)