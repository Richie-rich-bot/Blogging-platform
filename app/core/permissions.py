from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

# class AllowObjectOwners(BasePermission):
#     def has_object_permission(self, request, view,obj):
#         # if request.method in ['list', 'retrieve']:
#         return obj.author == request.user
    
class AllowObjectOwners(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user    