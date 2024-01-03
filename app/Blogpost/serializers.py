from rest_framework import serializers
from core.models import BlogPost, Comment

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment."""
    class Meta:
        model = Comment
        fields = ['id','text', 'created_at','post']
        
        
class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer for BlogPost."""
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'pub_date', 'author', 'likes', 'views','image']
        read_only_fields = ['id']        
        
        
class DetailCommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment."""
    post = BlogPostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id','text', 'created_at','post']



class BlogPostDetailSerializer(BlogPostSerializer):
    """Serializer for blog post detail view"""
    class Meta(BlogPostSerializer.Meta):
        fields = BlogPostSerializer.Meta.fields + ['content']