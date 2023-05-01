from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone

class UsersCountView(APIView):
    def get(self, request):
        users_count = User.objects.count()
        return Response({'count': users_count})

def last_login_api(request, user_id):
    print(user_id)
    try:
        print("hola")
        user = User.objects.get(id=user_id)
        print(user.email)
        last_login = user.last_login.strftime("%Y-%m-%d %H:%M:%S")
        print(last_login)
        response_data = {"last_login": last_login}
        return JsonResponse(response_data)
    except User.DoesNotExist:
        response_data = {"error": "No existe un usuario con el ID proporcionado."}
        return JsonResponse(response_data, status=404)