from .models import *
from vw_app.models import *
from rest_framework.views import APIView
from .serializers import SignupSerializer
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')
    def get(self, request):
        return render(request, 'accounts/login.html')

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        user_type = request.data.get('user_type')
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data.get('username'))
            profile = Profile.objects.create(user=user,user_type=user_type)
            profile.save()
            if user_type == 'Premium':
                    # premium user wallet
                    initial_amount=2500
                    wallet = Wallet(user=user,balance=initial_amount)
                    wallet.save()
            else:
                # Non premium user wallet
                initial_amount=1000
                wallet = Wallet(user=user,balance=initial_amount)
                wallet.save()
            login(request, user)
            return redirect('home')
        
        return redirect('signup')
    def get(self, request):
        return render(request, 'accounts/signup.html')
    

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('login')
