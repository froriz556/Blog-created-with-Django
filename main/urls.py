from django.urls import path
from .views import MainHome, PostView, PostAdd

app_name = 'main'
urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('posts/<slug:slug>/', PostView.as_view(), name='post_detail'),
    path('add_post/', PostAdd.as_view(), name='post_add'),
]