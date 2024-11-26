from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SleepRecord, HRVData

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'birth_date', 'is_staff')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_staff', 'is_active', 'groups')

@admin.register(SleepRecord)
class SleepRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time', 'quality_score')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username',)

@admin.register(HRVData)
class HRVDataAdmin(admin.ModelAdmin):
    list_display = ('sleep_record', 'timestamp', 'value')
    list_filter = ('sleep_record__user',)
