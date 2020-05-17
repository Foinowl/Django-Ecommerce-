from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
