from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing the serializer"""
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for user model"""
    class Meta:
        model=models.UserProfile
        fields = ('id','name','email','password')
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validatied_data):
        """Create and Return a New User"""

        user=models.UserProfile(
            email=validatied_data['email'],
            name=validatied_data['name']
        )
        user.set_password(validatied_data['password'])
        user.save()

        return user

class FlickrImagesSerializer(serializers.ModelSerializer):
    """Serializer for Flickr Images"""
    class Meta:
        model=models.FlickrImagesByGroup
        fields = ('id','group_id','group_name','user_profile_id','image')
        # extra_kwargs={'group_name':{'allow_null':False}}
    
       