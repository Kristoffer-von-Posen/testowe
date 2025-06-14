"""
URL configuration for proba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('helloworld.urls', 'helloworld'),
                     namespace='helloworld')),
    path('Nowyrok/', include(('Nowyrok.urls', 'Nowyrok'),
                             namespace='Nowyrok')),
    path('tasks/', include(('tasks.urls', 'tasks'), namespace='tasks')),
    path('lot/', include(('lotnisko.urls', 'lotnisko'), namespace='lotnisko')),
    path('Fischlein/',
         include(('Fischlein.urls', 'Fischlein'), namespace='Fischlein')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('java/', include(('java.urls', 'java'), namespace='java')),
    path('szachy/', include(('szachy.urls', 'szachy'), namespace='szachy'))
]
