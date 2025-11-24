from django.urls import path

from users.views import RegisterView, CustomUserLoginView, EmailConfirmView

app_name = 'users'
urlpatterns = [
    path('create_account/', RegisterView.as_view(), name='register'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('create_account/email_confirm/', EmailConfirmView.as_view(), name='email_confirm')
]