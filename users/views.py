from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.forms import RegisterForm, LoginForm
from users.models import CustomUser


class RegisterView(CreateView):

    model = CustomUser
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main:home')

class CustomUserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main:home')
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('users:profile')


