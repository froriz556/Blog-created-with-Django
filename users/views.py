from datetime import timezone

from Scripts.bottle import request
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.forms import RegisterForm, LoginForm, EmailConfirmForm
from users.models import CustomUser, EmailCodeVerification
from .services.send_email_code import send_code


class RegisterView(CreateView):

    model = CustomUser
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:email_confirm')

class CustomUserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main:home')
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('users:profile')

class EmailConfirmView(FormView):

    template_name = 'users/email_confirm.html'
    form_class = EmailConfirmForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        code = form.cleaned_data['code']
        user = self.request.user

        try:
            obj = EmailCodeVerification.objects.filter(
                user=user,
                code=code
            ).latest("create_time")

        except EmailCodeVerification.DoesNotExist:
            form.add_error("code", "Неверный код подтверждения")
            return self.form_invalid(form)

        if timezone.now() > obj.end_time:
            form.add_error('Срок действия кода истек')
            return self.form_invalid(form)

        if not obj.is_used:
            form.add_error('Указанный код не действителен')
            return self.form_invalid(form)

        user.is_active = True
        user.save()

        obj.is_used = True
        obj.save()

        messages.success(self.request, "Почта успешно подтверждена!")
        return super().form_valid(form)


