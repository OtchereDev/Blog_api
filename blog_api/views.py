from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from . import serializers
# Create your views here.

class PostListView(generics.ListCreateAPIView):
    serializer_class= serializers.PostSerializer
    queryset=Post.objects.all()
