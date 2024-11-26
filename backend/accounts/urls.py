from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import landing, register, SleepRecordViewSet, HRVDataViewSet

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
