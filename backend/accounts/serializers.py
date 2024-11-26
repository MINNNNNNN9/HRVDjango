from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import SleepRecord, HRVData

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone', 'birth_date')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'phone': {'required': False},
            'birth_date': {'required': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class SleepRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepRecord
        fields = ('id', 'start_time', 'end_time', 'quality_score', 'created_at')
        read_only_fields = ('created_at',)

class HRVDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRVData
        fields = ('id', 'sleep_record', 'timestamp', 'value', 'notes')
