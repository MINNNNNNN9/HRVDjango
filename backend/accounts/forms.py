from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='帳號',
        error_messages={
            'unique': '此帳號已被使用',
            'required': '請輸入帳號',
            'max_length': '帳號不能超過15個字元',
            'invalid': '帳號只能包含字母、數字和 @/./+/-/_'
        }
    )
    
    password1 = forms.CharField(
        label='密碼',
        widget=forms.PasswordInput,
        error_messages={
            'required': '請輸入密碼',
        }
    )
    
    password2 = forms.CharField(
        label='確認密碼',
        widget=forms.PasswordInput,
        error_messages={
            'required': '請再次輸入密碼',
        }
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        # 自定義密碼規則
        if len(password1) < 6:  # 改為最少6個字元
            raise ValidationError('密碼長度至少需要6個字元')
            
        if password1.isdigit():
            raise ValidationError('密碼不能全為數字')
            
        # 可以移除或修改其他規則
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError('兩次輸入的密碼不相符')
        return password2

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')
