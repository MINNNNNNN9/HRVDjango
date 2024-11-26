from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer

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

@api_view(['POST'])
@permission_classes([AllowAny])  # 添加這行
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
