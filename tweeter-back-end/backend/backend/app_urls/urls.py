# myapp/urls.py

from django.urls import path
from ..views.views import AcceptFriendRequestView, CommentCreateView, CommentLikeCreateView, FriendRequestListView, FriendsPostList, PostCreateView, PostLikeCreateView, RejectFriendRequestView, RemoveFriendView, SendFriendRequestCreateView, UserCreateView, UserList, PostList, CommentListByPostID, UserLoginView

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('comments/<int:post_id>/', CommentListByPostID.as_view(), name='comment-list-by-post-id'),
    path('friends/posts/<int:user_id>/', FriendsPostList.as_view(), name='friends-post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/like/', PostLikeCreateView.as_view(), name='post-like-create'),
    path('comments/<int:comment_id>/like/', CommentLikeCreateView.as_view(), name='comment-like-create'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('friend-request/send/', SendFriendRequestCreateView.as_view(), name='friend-request-create'),
    path('friend-request/accept/', AcceptFriendRequestView.as_view(), name='friend-request-accept'),
    path('friend-request/reject/', RejectFriendRequestView.as_view(), name='friend-request-reject'),
    path('friend-request/get-all-pending/<int:user_id>/', FriendRequestListView.as_view(), name='friend-request-list'),
    path('friend-request/remove/', RemoveFriendView.as_view(), name='friend-request-remove'),

]
