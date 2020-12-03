from blog.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['category',
                'title',
                'excerpt',
                'content',
                'slug',
                'author',
                'status',]