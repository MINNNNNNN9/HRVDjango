from django.urls import path
from . import views

# 確保 urlpatterns 是一個列表
urlpatterns = [
    path('', views.landing, name='api-landing'),
]
