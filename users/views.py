from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm
from users.models import CustomUser


class RegisterView(CreateView):

    model = CustomUser
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main:home')

