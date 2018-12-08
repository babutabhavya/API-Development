from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to update its profile"""
    def has_object_permission(self,request,view,object):
        """Checks if a user is trying to edit their own profiles"""
        #only safe http methods are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        #if object id is equal to the authenticated user id then return True else False
        return object.user_profile_id==request.user.id