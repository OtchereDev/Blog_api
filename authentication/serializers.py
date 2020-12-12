from rest_framework import serializers
from blog.models import Author

class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=255)
    last_name=serializers.CharField(max_length=255)
    user_name=serializers.CharField(max_length=255)
    email=serializers.EmailField(max_length=255)
    password=serializers.CharField(write_only=True,min_length=8,max_length=64)

    class Meta:
        model=Author
        fields=['first_name','last_name','user_name','email','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        if Author.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already in use')})

        return attrs

    def create(self,validated_data):
        return Author.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True,min_length=8,max_length=64)
    
    class Meta:
        model=Author
        fields=['email','password']
