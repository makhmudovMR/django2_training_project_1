from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Tutorial
# Create your views here.
class HomePage(View):

    def get(self, request):
        context = {'tutorial': Tutorial.objects.all()}
        return render(request, template_name='main/home.html', context=context)


