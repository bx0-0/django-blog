from django.urls import path
from .views import PostListView

app_name = 'index'

urlpatterns = [
    path('home/',PostListView.as_view(), name='home')
]