from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
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
