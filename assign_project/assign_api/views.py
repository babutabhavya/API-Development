from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from . import models
from . import permissions
from rest_framework.authtoken.models import Token

""" The Assignment Code Begins Below"""


class LoginViewSet(viewsets.ViewSet):
    """checks Email and Password and returns an token"""
    
    serializer_class=AuthTokenSerializer
    
    def create(self,request):
        """Use ObtainAuthToken to validate and return a token"""
        return ObtainAuthToken().post(request)

class FlickerImagViewSetGroup(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.FlickrImagesSerializer
    permission_classes=(permissions.UpdateOwnProfile,)
    def get_queryset(self):
        user=self.request.user
        groupid = self.request.query_params['group_id']
        if groupid is not None:
                queryset=models.FlickrImagesByGroup.objects.filter(user_profile=user,group_id=groupid)
                return queryset
        try:
            queryset=models.FlickrImagesByGroup.objects.filter(user_profile=user)
        except: 
            return Response({'error':'Invalid User. Authentication Token Missing or Invalid'})
        return queryset
    
    # def list(self,request,format=None):
        
    #     userprofile=self.request.user
        
    #     try:
    #         """This try Block Checks if any Parameters have been Passed in the URL. If No Parameters throws KeyError Exception"""
            
    #         a=request.query_params['group_id']
    #         try:
    #             queryset=models.FlickrImagesByGroup.objects.filter(user_profile=userprofile,group_id=a)
                
    #         except:
    #             return Response({'error':'Invalid User. Authentication Token Missing or Invalid'})
    #         Images=queryset.values()
    #         return Response({'user':userprofile.email,'queryset':Images})
        
        
    #     except:
           
    #         """This Except Block Handles The KeyError Exception By Passing All The Objects for the Current User"""
    #         try:
    #             queryset=models.FlickrImagesByGroup.objects.filter(user_profile=userprofile)
    #         except:
    #             return Response({'error':'Invalid User. Authentication Token Missing or Invalid'})
    #         Images=queryset.values()
    #         #Response is to be passed a dictionary that is converted into JSON
    #         return Response({'message':'Hello API','user':userprofile.email,'queryset':Images})
    
    def retrieve(self,request,pk):
        """Handles by getting an object using an id"""
        
        userprofile=self.request.user
        queryset=models.FlickrImagesByGroup.objects.filter(user_profile=userprofile,group_id=pk)
        
        Images=queryset.values()
        
        #Response is to be passed a dictionary that is converted into JSON
        return Response({'user':userprofile.email,'queryset':Images})  

         
class FlickerImagViewSetPhoto(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.FlickrImagesSerializer
    permission_classes=(permissions.UpdateOwnProfile,)
    def get_queryset(self):
        user=self.request.user
        try:
            queryset=models.FlickrImagesByGroup.objects.filter(user_profile=user)
            
        except: 
            return Response({'error':'Invalid User. Authentication Token Missing or Invalid'})
        return queryset
    
    # def list(self,request,format=None):
    #     """Handles By Getting All The Images Corresponding to the User Token In The HTTP HEADER"""
        
    #     userprofile=self.request.user
    #     try:
    #         queryset=models.FlickrImagesByGroup.objects.filter(user_profile=userprofile)
    #     except: 
    #         return Response({'error':'Invalid User. Authentication Token Missing or Invalid'})
    #     Images=queryset.values()
        
    #     #Response is to be passed a dictionary that is converted into JSON
    #     return Response({'user':userprofile.email,'queryset':Images}) 

    def retrieve(self,request,pk):
        """Handles By Getting All The Images Corresponding to the User Token In The HTTP HEADER as Well The Id Passed in the URL"""
        userprofile=self.request.user
        try:
            queryset=models.FlickrImagesByGroup.objects.filter(user_profile=userprofile,id=pk)
            
        except: 
            return Response({'error':'Invalid User. Authentication Token Missing or Invalid'})
        Images=queryset.values()
        
        #Response is to be passed a dictionary that is converted into JSON
        return Response({'user':userprofile.email,'queryset':Images})  
        
class Logout(APIView):
    """This View Returns The Logged Out Token Passed In The HTTP HEADER"""
    authentication_classes=(TokenAuthentication,)
    def get(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split(' ')
        token=token[1]
        tokens=Token(key=token)
        tokens.delete()
        return Response({'token':token,'Message':'You have be have been successfully logged out!'})
        

"""Practice Code"""
"""Please Ignore"""
"""Just for Reference as well as Testing"""

class HelloApi(APIView):
    """API VIEW"""
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        
        an_apiview=[
        'Uses HTTP Methods as functions GET,POST,PATCH,DELETE',
        'Similar To A Tradition Django View',
        'Gives you control over your logic',
        'is manually mapped to url'
        ]
        userprofile=self.request.user
    
        #Response is to be passed a dictionary that is converted into JSON
        return Response({'message':'Hello API','an_apiview':an_apiview,'user':userprofile.email})

    def post(self,request):
        serializer=serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class HelloViewSets(viewsets.ViewSet):
    """Test View Set"""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        an_apiviewset=[
            'Uses actions like (list,create,retirieve,update,partial_update)',
            'Automatically maps urls using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello','an_apiviewset':an_apiviewset})
    
    def create(self,request):
        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        """Handles by getting an object using an id"""
        return Response({'message':'GET'})

    def update(self,request,pk=None):
        """Handles by updating an object using an id"""
        return Response({'message':'PUTT'})

    def destroy(self,request,pk=None):
        """Handles by deleting an object using an id"""

        return Response({'message':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ModelViewSet is used for creating and updating user profiles"""
    
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
