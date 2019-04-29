from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
            login(request, user)
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, 'main/register.html', context={'form': form})
            


    def get(self, request):
        form = UserCreationForm
        return render(request, 'main/register.html', context={'form': form})
