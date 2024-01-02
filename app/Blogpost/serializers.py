from rest_framework import serializers
from core.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer for BlogPost."""
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'pub_date', 'author', 'likes', 'views',
        ]
        read_only_fields = ['id']