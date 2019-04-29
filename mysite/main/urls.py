from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('register/', RegisterPage.as_view(), name='register')
]