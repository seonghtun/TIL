from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.posts, name="posts"),
    path("list/", views.post_list, name="post_list"),
    path("<int:post_id>/", views.post_detail, name="post_detail"),
    path("add/",views.post_add, name="post_add"),
]