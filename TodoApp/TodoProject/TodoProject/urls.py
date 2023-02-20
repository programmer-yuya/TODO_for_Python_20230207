"""TodoProject URL Configuration

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
from django.urls import path, include # includeを追加

urlpatterns = [
    path("TodoApp/", include("TodoApp.urls")),
    path("TestApp2/", include("TestApp2.urls")),
    path("TestApp3/", include("TestApp3.urls")),
    path("TestApp/", include("TestApp.urls")),
    path("admin/", admin.site.urls),
 ]
