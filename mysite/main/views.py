from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class HomePage(View):

    def get(self, request):
        return HttpResponse('Hello is\'t django app')