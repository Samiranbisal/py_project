"""
URL configuration for newapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from newapp import views
from newapp import tatai

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('about/', views.aboutUs),
    path('about/<couseid>', views.couseDetails),
    path('tatai/', tatai.sb),
    path('aboutus/',views.about),
    path('from/', views.userform),
    path('newes/<nid>', views.NewsDeatails)
]
