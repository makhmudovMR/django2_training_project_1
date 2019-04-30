from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('tutorialseries/<str:category_slug>', TutorialSeriesPage.as_view(), name='tutorial_series'),
    path('tutorials/<int:id>', TutorialPage.as_view(), name='tutorials'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutRequest.as_view(), name='logout'),
    path('login/', LoginPage.as_view(), name='login')
]