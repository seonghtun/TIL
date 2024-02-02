from django.urls import path
from . import views

app_name='posts'
urlpatterns=[
    path("feeds/", views.feeds,name="feeds"),
    path("comment_add/", views.comment_add, name="comment_add"),
    path("comment_delete/<int:comment_id>/", views.comment_delete, name="comment_delete"),
    path("post_add/", views.post_add, name="post_add"),
]