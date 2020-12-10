from blog.models import Post,Category
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['category',
                'title',
                'excerpt',
                'content',
                'author',
                'status',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'

