from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import flickrapi
from django.contrib.auth.models import User

# Create your models here.

class UserProfileManager(BaseUserManager):
    """helps django work with our custom user model"""

    def create_user(self,email,name,password=None):
       
        """creates a new user in the system"""
       
        #users must have an email address
        if not email :
            raise ValueError('Users must have an email address')
       
        #normalises the email (converting the any uppercases in the email to lowercases)     
        email=self.normalize_email(email)
       
        user=self.model(email=email,name=name)
       
        #converts the password into hash and stores into the database for security
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,name,password):
       
        #creates a superuser with the given email"""
       
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True

        user.save(using=self.db)

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """respresnts a user profile inside our system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_fullname(self):
        """function to get the full name of the user"""
        return self.name
    
    def __str__(self):
        """function to return an object as a  string"""
        return self.email

class FlickrImagesByGroup(models.Model):
    """"Image Model"""
    group_id = models.CharField(max_length=25)
    group_name = models.CharField(max_length=25)
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    
    objects=models.Manager()
   
    def get_group_name(self):
        return self.group_name
    def get_group_if(self):
        return self.group_id
    def __str__(self):
        return self.group_name

