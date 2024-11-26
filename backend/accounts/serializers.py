from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import SleepRecord, HRVData

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirm_password', 'phone', 'birth_date')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'phone': {'required': False},
            'birth_date': {'required': False}
        }

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({'confirm_password': '兩次輸入的密碼不相符'})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
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
