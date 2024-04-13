from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.profile),
    path("about/", views.about),
    path("support/", views.support),
    path("posts/", views.posts),
    path("post/<int:post_id>", views.single_post, name="single_post"),
    path("add/", views.add_post),
]
