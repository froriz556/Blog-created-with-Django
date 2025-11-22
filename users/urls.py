from django.urls import path

from users.views import RegisterView, CustomUserLoginView

app_name = 'users'
urlpatterns = [
    path('create_account/', RegisterView.as_view(), name='register'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
]