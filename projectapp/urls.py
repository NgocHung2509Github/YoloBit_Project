"""
URL configuration for projectapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # when data send to the endpoints, call the functions in views.py
    path('fanswitch/', views.FanSwitchView.as_view(), name='fanswitch'),
    path('lightswitch/', views.LightSwitchView.as_view(), name='lightswitch'),
    path('temperature/', views.TemperatureView.as_view(), name='temperature'),
    path('status/', views.DetectView.as_view(), name='status'),
    path('name/', views.NameView.as_view(), name='name'),
    path('', views.index, name='index')
]
