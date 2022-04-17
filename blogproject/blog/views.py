from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Post, Tag
import markdown
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from .form import CommentForm
from django.contrib import messages

# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    return render(request, "blog/index.html", {"post_list": post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        TocExtension(slugify=slugify),
    ])

    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ""

    return render(request, "blog/detail.html", {"post": post})


def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month,).order_by("-created_time")
    return render(request, "blog/index.html", {"post_list": post_list})

def category(request, pk):
    c = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=c).order_by("-created_time")
    return render(request, "blog/index.html", {"post_list": post_list})

def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tag=t).order_by("-created_time")
    return render(request, "blog/index.html", {"post_list": post_list})

def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request, messages.SUCCESS, "评论发表成功！", extra_tags="success")
        return HttpResponseRedirect(reverse("blog:detail", args=(post_id,)))

    messages.add_message(request, messages.ERROR, "评论发表失败！请修改表单中的错误后重新提交", extra_tags="danger")
    return render(request, "blog/preview.html", {"post": post, "form": form})