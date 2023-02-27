from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from account.models import User
from account.api.serializers import UserGameSerializer




# Create your views here.
@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


#'''
@csrf_exempt
def userGameAPI(request,id=0):
    if request.method=='GET':
        user_id = request.GET['username']
        users = User.objects.all() 
        user_serializer = UserGameSerializer(users,many=True)
        data = user_serializer.data

        #data[0]['username'] # this returns the first username in the whole database.

        return JsonResponse(data[0], safe=False)
#'''

'''
@csrf_exempt
def userGameAPI(request):
    if request.method=='GET':
        id = request.GET(user_id)
        users = User.objects.get(usename=id) 
        user_serializer = UserGameSerializer(users,many=True)
        return id
#'''