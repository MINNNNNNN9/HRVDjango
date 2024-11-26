"""
URL configuration for hrvproject project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import landing, register, SleepRecordViewSet, HRVDataViewSet

# 創建 router
router = DefaultRouter()
router.register(r'sleep-records', SleepRecordViewSet, basename='sleep-record')
router.register(r'hrv-data', HRVDataViewSet, basename='hrv-data')

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/register/', register, name='register'),
]
