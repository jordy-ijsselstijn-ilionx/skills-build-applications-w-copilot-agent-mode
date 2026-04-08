"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, WorkoutViewSet, ActivityViewSet, LeaderboardViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboards', LeaderboardViewSet)

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
def get_base_url(request):
    if CODESPACE_NAME:
        return f'https://{CODESPACE_NAME}-8000.app.github.dev/api/'
    return request.build_absolute_uri('/api/')

@api_view(['GET'])
def api_root(request, format=None):
    base_url = get_base_url(request)
    return Response({
        'users': f'{base_url}users/',
        'teams': f'{base_url}teams/',
        'workouts': f'{base_url}workouts/',
        'activities': f'{base_url}activities/',
        'leaderboards': f'{base_url}leaderboards/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
