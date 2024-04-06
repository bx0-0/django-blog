from django.urls import path
from .views import PostDetailView, PostCreateView, YourPostsListView, PostUpdateView

app_name = 'single_blog'
urlpatterns = [
    path('add/',PostCreateView.as_view(),name='add-post'),
    path('my-posts/',YourPostsListView.as_view(),name='my-posts'),
    path('<str:slug>/',PostDetailView.as_view(),name='post'),
    path('edit/<str:slug>', PostUpdateView.as_view(),name='post-update'),
]