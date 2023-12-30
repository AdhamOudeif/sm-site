# myapp/models.py

from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.EmailField()
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Birthdate = models.DateField()
    Gender = models.CharField(max_length=10)
    ProfilePicture = models.CharField(max_length=255)
    RegistrationDate = models.DateTimeField()
    class Meta:
        app_label = 'backend'
        db_table = 'user'

class Post(models.Model):
    PostID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, db_column='UserID')
    Content = models.TextField()
    Photo = models.CharField(max_length=255)
    Timestamp = models.DateTimeField()
    LikesCount = models.IntegerField()
    CommentsCount = models.IntegerField()
    SharesCount = models.IntegerField()
    class Meta:
        app_label = 'backend'
        db_table = 'post'        
