from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField(blank=True, db_index=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_username_url(self):
        return reverse('user-posts', kwargs={'username': self.author.username})
