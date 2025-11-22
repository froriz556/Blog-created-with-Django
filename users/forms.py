from django.contrib.auth import authenticate, login

from .models import CustomUser
from django import forms

class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Указанный адрес электронной почты уже занят')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Указанное имя пользователя уже занято')
        return username

    def clean(self):

        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('password1')

        if p1 != p2:
            raise forms.ValidationError('Введеные пароли не совпадают.')

        return cleaned

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError("Неверный адрес электронной почты или пароль.")
        if not user.is_active:
            raise forms.ValidationError("Аккаунт не прошёл активацию, проверьте ваш почтовый ящик.")
        self.user = user

        return cleaned_data


