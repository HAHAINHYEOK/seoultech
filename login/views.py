from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from mysite import settings

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request, new_user)
			redirect_to = settings.LOGIN_REDIRECT_URL
			return redirect(redirect_to,{})
	else:
		form = UserForm()
		return render(request, 'login/signup.html', {'form':form})


def indexLogin(request):
	if request.method  == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			redirect_to = settings.LOGIN_REDIRECT_URL
			return redirect(redirect_to, {user})
		else:
			return HttpResponse('login failed')
	else:
		form = LoginForm()
		return render(request, 'login/index2_login.html', {'form':form})

def index(request):
	return render(request,'login/index.html')

def mainpage(request):
	return render(request,'course/main.html')

# Create your views here.
