from django.shortcuts import render,get_list_or_404
from rest_framework import generics
from blog.models import Post,Category
from . import serializers


class PostListView(generics.ListCreateAPIView):
    serializer_class= serializers.PostSerializer
    queryset=Post.objects.all()

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.PostSerializer
    lookup_field='id'
    queryset=Post.objects.all()


class CategoryCreateView(generics.ListCreateAPIView):
    serializer_class=serializers.CategorySerializer
    queryset=Category.objects.all()

class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.CategorySerializer
    lookup_field='id'
    queryset=Category.objects.all()


#user authentication 
# and jwt tokens
# and swagger ui for documentation
