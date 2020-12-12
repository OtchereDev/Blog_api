from django.conf import settings
from blog.models import Author

import jwt
from rest_framework import authentication
from rest_framework import exceptions

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        auth_data=authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix,token=auth_data.decode('utf-8').split(' ')
        
        try:
            payload=jwt.decode(token,settings.JWTSECRETEPASSWORD)
            user=Author.objects.get(email=payload['email'])
            return(user,token)
        except jwt.DecodeError as i:
            raise exceptions.AuthenticationFailed('Your token is invalid')
        except jwt.ExpiredSignatureError as i:
            raise exceptions.AuthenticationFailed('Your token has expired')
