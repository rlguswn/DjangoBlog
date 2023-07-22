from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일을 입력해주세요.'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호를 입력해주세요.'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'age']