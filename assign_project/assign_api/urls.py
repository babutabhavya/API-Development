
from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSets,base_name='hello-viewset')
"""when giving a model view set you dont need to specify the base no becuase django rest framework figures it out by using the model registered with the view set"""
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,base_name='login')
router.register('group',views.FlickerImagViewSetGroup,base_name='group') 
router.register('photo' ,views.FlickerImagViewSetPhoto ,base_name='photo')

urlpatterns = [

    url(r'^hello-view/',views.HelloApi.as_view()),
    url(r'^logout/',views.Logout.as_view()),
    url(r'' , include(router.urls))
]