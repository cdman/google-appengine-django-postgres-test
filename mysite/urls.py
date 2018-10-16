"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import logging

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.models import User

def test(request):
    logging.getLogger('django1').debug('debug1')
    logging.getLogger('django2').debug('debug2')
    logging.getLogger('django3').debug('debug3')
    logging.getLogger('django4').debug('debug4')

    cnt = User.objects.count()
    return HttpResponse('Count: %d' % cnt)


urlpatterns = [
    path('', test),
]
