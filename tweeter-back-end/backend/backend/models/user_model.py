# models/user_model.py

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
