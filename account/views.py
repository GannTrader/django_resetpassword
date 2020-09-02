from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def loginUser(request):
	form = LoginForm
	return render(request, 'account/login.html', {'form': form})

def postloginUser(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(request, username = username, password = password)
	if user is not None:
		login(request, user)
		return HttpResponse('success')
	else:
		return HttpResponse('fail login')
