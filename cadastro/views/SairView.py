from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

class SairView(LogoutView):
    redirect_authenticated_user = True
    