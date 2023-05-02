from django.shortcuts import render
import pytz
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
utc_tz = pytz.utc
local_tz = pytz.timezone('America/New_York')

class UsersCountView(APIView):
    def get(self, request):
        users_count = User.objects.count()
        return Response({'count': users_count})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def last_login_api(request, user_id):
    print('entró')
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'El usuario no existe'})
    
    last_login = user.last_login.astimezone(utc_tz).astimezone(local_tz).strftime('%Y-%m-%d %H:%M:%S')
    
    return JsonResponse({'last_login': last_login})