from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from posts.models import Post, Comment, PostImage, HashTag
from . import forms
from django.views.decorators.http import require_POST
from django.urls import reverse


# Create your views here.
def feeds(request):
    user = request.user

    # is_authenticated = user.is_authenticated

    # print("user:", user)
    # print("is_authenticated:", is_authenticated)

    if not request.user.is_authenticated:
        return redirect("users:login")
    
    posts = Post.objects.all()
    comment_form = forms.CommentForm()
    context = {
        "posts": posts,
        "comment_form": comment_form,}
    return render(request,"posts/feeds.html", context)

@require_POST # 댓글 작성을 처리할 View, Post 요청만 허용
def comment_add(request):

    form = forms.CommentForm(data=request.POST)
    if form.is_valid():
        # commit=False 옵션으로 메모상에 Comment 객체 생성
        comment = form.save(commit=False)

        # Comment 생성에 필요한 사용자 정보를 request에서 가져와 할당
        comment.user = request.user

        comment.save()

        # print(comment.id)
        # print(comment.content)
        # print(comment.user)
        # print(comment.post)
        # if request.GET.get("next"):
        #     url_next = request.GET.get("next")
        # else :
        #     url_next = reverse("posts:feeds") + f"#post-{comment.post.id}"
        
        url_next = request.GET.get('next')
        return HttpResponseRedirect(url_next)

@require_POST
def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if comment.user == request.user:
            comment.delete()
            url = reverse("posts:feeds") + f"#post-{comment.post.id}"
            return HttpResponseRedirect(url)
        else:
            return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")

def post_add(request):
    if request.method == "POST":
        # request.POST로 온 데이터 ("content")는 PostForm으로 처리
        form = forms.PostForm(request.POST)

        if form.is_valid():
            # Post의 "user" 값은 request에서 가져와 자동 할당한다.
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            #Post를 생성한 후
            # request.FILES.getlist("images")로 전송된 이미지들을 순회하며 PostImage 객체를 생성한다.
            for image_file in request.FILES.getlist("images"):
                # request.FILES 또는 request.FILES.getlist()로 가져온 파일은
                # Model의 ImageField 부분에 곧바로 할당한다.
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )

            # "tags"에 전달된 문자열을 분리해 HashTag 생성
            tag_string = request.POST.get("tags")
            if tag_string:
                tag_names = {tag_name.strip() for tag_name in tag_string.split(',')}
                for tag_name in tag_names:
                    tag, _ = HashTag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)
            url = f"{reverse('posts:feeds')}#post-{post.id}"
            return HttpResponseRedirect(url)
    else:
        form = forms.PostForm()
    context = { "form" : form }
    return render(request, "posts/post_add.html", context)

def tags(request, tag_name):
    try:
        tag = HashTag.objects.get(name=tag_name)
    except HashTag.DoesNotExist:
        # tag_name에 해당하는 HashTag를 찾지 못한 경우, 빈 QuerySet을 돌려준다.
        posts= Post.objects.none()
    else :
        #tags (M2M 필드)에 찾은 HashTag 객체가 있는 필터
        posts = Post.objects.filter(tags=tag)

    context = {
    "tag_name" : tag_name,
    "posts" : posts,
    }
    return render(request, 'posts/tags.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = forms.CommentForm()
    context = {
        "post": post,
        "comment_form" : comment_form,
        }
    return render(request, "posts/post_detail.html", context)

def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    # 사용자가 "좋아요를 누른 Post 목록"에 "좋아요 버튼을 누른  Post"가 존재한다면
    if user.like_posts.filter(id=post.id).exists():
        # 좋아요 목록에서 삭제한다
        user.like_posts.remove(post)
    # 존재하지 않는다면 좋아요 목록에 추가
    else:
        user.like_posts.add(post)
    
    # next로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 피드 페이지에서 해당 Post 위치로 이동
    url_next = request.GET.get("next") or reverse("posts:feeds") + f"#post-{post.id}"
    return HttpResponseRedirect(url_next)