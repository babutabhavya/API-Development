
import os
import sys
from django.core.wsgi import get_wsgi_application
import flickrapi

# from django.utils import timezone
# from django.conf import settings

# derive location to  django project setting.py
proj_path='/Users/bhavyababuta/Desktop/workspace/assign_proj/assign_project'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assign_project.settings")
sys.path.append(proj_path)

application = get_wsgi_application()
from django.contrib.auth.models import User
from assign_api.models import UserProfile
from assign_api.models import FlickrImagesByGroup

def sync_flickr_photos():
        api_key = u'ad070b9c48feb64a4b87d7724b1c8c0c'
        api_secret = u'cf7a5d034397056e'
        groupid=4
        groupname=''
        flickr = flickrapi.FlickrAPI(api_key, api_secret)
        photos = flickr.groups.pools.getPhotos(group_id='80641914@N00') 
        for e in UserProfile.objects.filter(email='babutabhavya@gmail.com'):
            user=e
        for i in range (len(photos[0])):
            if i<=(len(photos[0]))/4:
                groupid=1
                groupname='HelloFlickr1'
            if i>len(photos[0])/4 and i<=(len(photos[0]))*2/4:
                groupid=2
                groupname='HelloFlickr2'
            if i>len(photos[0])*2/4 and i<=(len(photos[0]))*3/4:
                groupid=3
                groupname='HelloFlickr3'
            if i>len(photos[0])*3/4 and i<=(len(photos[0])):
                groupid=4
                groupname='HelloFlickr4'
            Image = FlickrImagesByGroup(group_id=str(groupid),
                group_name=groupname,
                user_profile=user,
                image=str(photos[0][i].get('id')))
            Image.save()
sync_flickr_photos()