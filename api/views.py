import requests
from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 
from dj_rest_auth.utils import jwt_encode
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse 
from django.contrib.auth import get_user_model
from .models import * 
from .serializers import * 
# Create your views here.

class GoogleLogin(APIView):
    def get(self, request):
        google_auth_url = (
            "https://accounts.google.com/o/oauth2/v2/auth?"
            f"client_id={settings.CLIENT_ID}&"
            f"redirect_uri={settings.GOOGLE_REDIRECT_URI}&"
            "response_type=code&"
            "scope=email profile"
        )
        return redirect( google_auth_url )
    
@api_view( [ 'GET' ] )
def google_callback( request : Request ):
    code = request.GET.get( 'code' )
    if not code:
        return JsonResponse( {'error': 'No code provided' } , status = status.HTTP_400_BAD_REQUEST )
    
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        'code': code,
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }

    token_response = requests.post( token_url , data = token_data )
    token_json = token_response.json()

    if 'error' in token_json:
        return JsonResponse({'error': token_json['error']}, status = status.HTTP_400_BAD_REQUEST )

    access_token = token_json.get( 'access_token' )
    id_token_str = token_json.get( 'id_token' )

    token_info_url = f"https://oauth2.googleapis.com/tokeninfo?id_token={id_token_str}"
    token_info_response = requests.get( token_info_url )
    idinfo = token_info_response.json()

    if 'error' in idinfo:
        return JsonResponse( { 'error' : idinfo[ 'error' ] } , status = status.HTTP_400_BAD_REQUEST )

    user_id = idinfo[ 'sub' ]
    email = idinfo[ 'email' ]
    User = get_user_model()
    user, created = User.objects.get_or_create( email = email , defaults = { 'username': email } )
    token = str( jwt_encode( user ) )   
    return JsonResponse( { 'token' : token , 'user_id' : user.id } , status = status.HTTP_200_OK )



