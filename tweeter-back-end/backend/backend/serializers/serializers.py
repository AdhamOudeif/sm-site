from rest_framework import serializers
from ..models.models import User, Post, Comment, Friendship
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    # Map lowercase payload keys to model fields
    userid = serializers.IntegerField(source='UserID', read_only=True)
    username = serializers.CharField(source='Username')
    email = serializers.EmailField(source='Email')
    password = serializers.CharField(source='Password', write_only=True)
    firstName = serializers.CharField(source='FirstName')
    lastName = serializers.CharField(source='LastName')
    birthdate = serializers.DateField(source='Birthdate')
    gender = serializers.CharField(source='Gender')
    profilepicture = serializers.CharField(source='ProfilePicture', required=False)
    registrationdate = serializers.DateTimeField(source='RegistrationDate', read_only=True)

    class Meta:
        model = User
        fields = [
            'userid', 'username', 'email', 'password', 'firstName',
            'lastName', 'birthdate', 'gender', 'profilepicture', 'registrationdate'
        ]

class PostSerializer(serializers.ModelSerializer):
    postid = serializers.IntegerField(source='PostID', read_only=True)
    userid = serializers.IntegerField(source='UserID.UserID')  # Access related field
    content = serializers.CharField(source='Content')
    photo = serializers.CharField(source='Photo', required=False)
    timestamp = serializers.DateTimeField(source='Timestamp')
    likescount = serializers.IntegerField(source='LikesCount')
    commentscount = serializers.IntegerField(source='CommentsCount')
    sharescount = serializers.IntegerField(source='SharesCount')

    class Meta:
        model = Post
        fields = [
            'postid', 'userid', 'content', 'photo', 'timestamp', 
            'likescount', 'commentscount', 'sharescount'
        ]

class CommentSerializer(serializers.ModelSerializer):
    commentid = serializers.IntegerField(source='CommentId', read_only=True)
    postid = serializers.IntegerField(source='PostID.PostID')  # Access related field
    userid = serializers.IntegerField(source='UserID.UserID')  # Access related field
    content = serializers.CharField(source='Content')
    timestamp = serializers.DateTimeField(source='Timestamp')
    likescount = serializers.IntegerField(source='LikesCount')

    class Meta:
        model = Comment
        fields = [
            'commentid', 'postid', 'userid', 'content', 
            'timestamp', 'likescount'
        ]

class FriendsPostList(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    userid = serializers.IntegerField(source='UserID.UserID')  # Access related field
    content = serializers.CharField(source='Content')
    photo = serializers.CharField(source='Photo', required=False)

    class Meta:
        model = Post
        fields = ['userid', 'content', 'photo']

class CommentCreateSerializer(serializers.ModelSerializer):
    userid = serializers.IntegerField(source='UserID.UserID')  # Access related field
    postid = serializers.IntegerField(source='PostID.PostID')  # Access related field
    content = serializers.CharField(source='Content')

    class Meta:
        model = Comment
        fields = ['userid', 'postid', 'content']

class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='Username')
    email = serializers.EmailField(source='Email')
    password = serializers.CharField(source='Password', write_only=True)
    firstName = serializers.CharField(source='FirstName')
    lastName = serializers.CharField(source='LastName')
    birthdate = serializers.DateField(source='Birthdate')
    gender = serializers.CharField(source='Gender')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'firstName', 
            'lastName', 'birthdate', 'gender'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['Password'] = make_password(validated_data['Password'])
        return User.objects.create(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class FriendRequestSerializer(serializers.ModelSerializer):
    user1id = serializers.IntegerField(source='User1ID.UserID')  # Access related field
    user2id = serializers.IntegerField(source='User2ID.UserID')  # Access related field

    class Meta:
        model = Friendship
        fields = ['user1id', 'user2id']
