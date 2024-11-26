from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import UserRateThrottle
from .serializers import UserSerializer, SleepRecordSerializer, HRVDataSerializer
from .models import SleepRecord, HRVData
import logging

logger = logging.getLogger(__name__)

class RegisterThrottle(UserRateThrottle):
    rate = '5/hour'

# 添加 ViewSet
class SleepRecordViewSet(viewsets.ModelViewSet):
    serializer_class = SleepRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SleepRecord.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HRVDataViewSet(viewsets.ModelViewSet):
    serializer_class = HRVDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HRVData.objects.filter(sleep_record__user=self.request.user)

@api_view(['GET'])
@permission_classes([AllowAny])
def landing(request):
    """
    首頁 API 端點
    """
    return Response({
        "message": "歡迎使用 HRV 睡眠監測平台",
        "version": "1.0.0",
        "endpoints": {
            "auth": {
                "register": "/api/auth/register/",
                "login": "/api/auth/login/"
            }
        }
    })

@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([RegisterThrottle])
def register(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            logger.info(f"New user registered: {user.username}")
            return Response({
                'status': 'success',
                'message': '註冊成功',
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        return Response({
            'status': 'error',
            'message': '註冊失敗',
            'errors': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            logger.info(f"User logged in: {username}")
            return Response({
                'success': True,
                'user': UserSerializer(user).data
            })
        return Response({
            'success': False,
            'message': '用戶名或密碼錯誤'
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return Response({
            'success': False,
            'message': '登入失敗'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    logout(request)
    return Response({'success': True})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_user(request):
    return Response(UserSerializer(request.user).data)
