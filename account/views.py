from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, forgotPassForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

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
def forgotPass(request):
	form = forgotPassForm
	return render(request, 'account/forgot-password.html', {'form': form})

def checkGmail(request):
	email = request.POST['email']
	user = User.objects.filter(email = email)

	if user.exists():
		return HttpResponse('exists')
	else:
		messages.info(request, 'email does not exits, please check that again!')
		return redirect('account:forgotPass')