from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


class RegisterView(APIView):
    
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('/home/')
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
        return redirect('/home/')

def LoginView(request):
    if(request.user.is_authenticated):
        return redirect('/home/')
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('password')
        if(uname != "" and password != ""):
            user = authenticate(username = uname, password = password)
            if(user != None):
                login(request, user)
                return redirect('/home/')
        else:
            return render(request, 'authenticate/login.html', {'msg' : 'Account Credentials are invalid.'})
    return render(request, 'authenticate/login.html', {'msg' : ''})

@login_required
def LogoutView(request):
    logout(request)
    return redirect('LoginView')
