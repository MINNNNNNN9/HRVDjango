from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])  # 允許未認證的訪問
def landing(request):
    return Response({
        "message": "Welcome to HRV Sleep Monitoring Platform API",
        "version": "1.0.0",
        "endpoints": {
            "auth": {
                "login": "/api/auth/login/",
                "register": "/api/auth/register/"
            },
            "sleep_records": "/api/sleep-records/",
            "hrv_data": "/api/hrv-data/"
        }
    })
