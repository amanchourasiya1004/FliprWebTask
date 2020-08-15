from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate


class RegisterView(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'authenticate/register.html', {'error' : '-'})

    def post(self, request, *args, **kwargs):
        input_data = {'username' : request.POST.get('username'), 'email' : request.POST.get('email'), 'password' : request.POST.get('password')}
        serializer = RegistrationSerializer(data = input_data)
        data = {}
        if(serializer.is_valid()):
            account = serializer.save()
            user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
            login(request, user)
            data['response'] = 'Successfully registered a user.'
        else:
            data = serializer.errors
        return Response(data)
