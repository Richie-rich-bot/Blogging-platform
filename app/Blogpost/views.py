from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,generics,mixins
from django.shortcuts import render
from core.permissions import AllowObjectOwners

from core.models import BlogPost, Comment
from .serializers import BlogPostDetailSerializer, BlogPostSerializer, CommentSerializer, DetailCommentSerializer

from rest_framework import filters

class BlogPostViewSet(viewsets.ModelViewSet):
    """View for manage blog APIs."""
    serializer_class = BlogPostDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,AllowObjectOwners]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        queryset = BlogPost.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogPostSerializer
        return self.serializer_class

class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """Viewset for managing comments."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, AllowObjectOwners]
    filter_backends = [filters.SearchFilter]
    search_fields = ['author']
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DetailCommentSerializer
        return self.serializer_class
