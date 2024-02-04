from django.contrib import admin
from posts.models import Post, PostImage, Comment, HashTag
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe
import admin_thumbnails
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

# AdminFileWidget은 관리자 페이지에서 '파일 선택' 버튼을 보여주는 부분이다.
# 이 widget을 커스텀하여, <img> 태그를 추가한다.
class InlineImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name,value, attrs, renderer)
        if value and getattr(value, "url", None):
            html = html + mark_safe(f'<img src="{value.url}" height="150">') 
        return html

# ImageField를 표시할 때, AdminFileWidget을 커스텀한 InlineImageWidget을 사용한다.
# class PostImageInline(admin.TabularInline):
#     model = PostImage
#     extra = 1
#     formfield_overrides = {
#         models.ImageField: {
#             "widget": InlineImageWidget,
#         }
#     }

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class LikeUserInline(admin.TabularInline):
    model = Post.like_users.through
    verbose_name = "좋아요 한 User"
    verbose_name_plural = f"{verbose_name} 목록"
    extra=1

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =[
        "id",
        "content",
    ]

    inlines = [
        CommentInline,
        PostImageInline,
        LikeUserInline,
    ]
    formfield_overrides ={
        ManyToManyField: {"widget": CheckboxSelectMultiple},
    }

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=[
        "id",
        "post",
        "content",
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass