from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'auth_user'
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]

class SleepRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                           on_delete=models.CASCADE,
                           related_name='sleep_records')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    quality_score = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
        ]

class HRVData(models.Model):
    sleep_record = models.ForeignKey(
        SleepRecord, 
        on_delete=models.CASCADE,
        related_name='hrv_readings'
    )
    timestamp = models.DateTimeField()
    value = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['timestamp']
        indexes = [
            models.Index(fields=['sleep_record', 'timestamp']),
        ]
