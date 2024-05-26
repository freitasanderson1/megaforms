from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'cadastro/login.html'
    