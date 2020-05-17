from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from allauth.utils import get_user_model
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# class PostCreateView(LoginRequiredMixin,ObjectCreateMixin,View):
#     model_form = PostForm
#     template = 'blog/post_form.html'
#
#
# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'slug', 'content', 'tags']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False