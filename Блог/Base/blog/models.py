from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to="media/", null=True)
    author_user_name = models.CharField(max_length=30, default="Anonymous post")

    def __str__(self):
        return self.title
