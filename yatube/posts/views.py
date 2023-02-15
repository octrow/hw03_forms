from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User
from .paginate_utils import paginate_posts


def index(request):
    post_list = Post.objects.select_related().all()
    page_obj = paginate_posts(post_list, request)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.select_related().all()
    page_obj = paginate_posts(post_list, request)
    context = {
        "group": group,
        "page_obj": page_obj,
    }
    return render(request, "posts/group_list.html", context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = (
        Post.objects
        .select_related('author', 'group')
        .filter(author=author)
        .order_by("-pub_date")
    )
    post_count = posts.count()
    page_obj = paginate_posts(posts, request)
    context = {
        "author": author,
        "page_obj": page_obj,
        "post_count": post_count,
    }
    return render(request, "posts/profile.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        return post_delete(request, post_id)
    context = {
        "post": post,
    }
    return render(request, "posts/post_detail.html", context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "GET" or not form.is_valid():
        context = {
            "form": form,
        }
        return render(request, "posts/create_post.html", context)
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect("posts:profile", username=request.user.username)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect("posts:post_detail", post_id=post.id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "GET" or not form.is_valid():
        context = {
            "form": form
        }
        return render(request, "posts/create_post.html", context)
    form.save()
    return redirect("posts:post_detail", post_id=post.id)


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        post.delete()
        return redirect("posts:profile", username=request.user.username)
    return redirect("posts:post_detail", post_id=post.id)
