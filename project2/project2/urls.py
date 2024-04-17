"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from calapp.views import index,RegisterInput,Register,Login,Contact,Log,cont
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index.as_view()),
    path('registerinput',RegisterInput.as_view()),
    path('register',Register.as_view()),
    path('login',Login.as_view()),
    path('contact',Contact.as_view()),
    path('log',Log.as_view()),
    path('cont',cont.as_view()),
]
