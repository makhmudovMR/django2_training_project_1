from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
class HomePage(View):

    def get(self, request):
        context = {'tutorial': Tutorial.objects.all()}
        return render(request, template_name='main/home.html', context=context)


class RegisterPage(View):

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account created {username}')
            login(request, user)
            messages.info(request, f'You are logged in ass {username}')
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f" {msg} {form.error_messages[msg]}")
            return render(request, 'main/register.html', context={'form': form})
            


    def get(self, request):
        form = UserCreationForm
        return render(request, 'main/register.html', context={'form': form})

class LogoutRequest(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Logout successfully')
        return redirect('main:homepage')

class LoginPage(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'main/login.html', context={'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST) # нужно разобраться с этим
        print('we are here')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print('USER: ',user)
            if user is not None:
                login(request, user)
                messages.info(request, f'Login success, Hello {user.username}')
                return redirect('main:homepage')
        return render(request, 'main/login.html', context={'form': form})