# from xml.etree.ElementTree import Comment
from django import template
from ..models import Post, Category, Tag, Comment
from ..form import CommentForm

register = template.Library()

@register.inclusion_tag("blog/inclusions/_recent_posts.html", takes_context=True)
def show_recent_posts(context, num=5):
    return {
        "post_list": Post.objects.order_by("-created_time")[:num]
    }

@register.inclusion_tag("blog/inclusions/_archives.html", takes_context=True)
def show_archives(context):
    return {
        "date_list": Post.objects.dates("created_time", "month", order="DESC")
    }

@register.inclusion_tag("blog/inclusions/_categories.html", takes_context=True)
def show_categories(context):
    return {
        "category_list": Category.objects.all()
    }

@register.inclusion_tag("blog/inclusions/_tags.html", takes_context=True)
def show_tags(context):
    return {
        "tag_list": Tag.objects.all()
    }

@register.inclusion_tag("blog/inclusions/_comments.html", takes_context=True)
def show_comments(context, post):
    comment_list = Comment.objects.filter(post=post).order_by("-created_time")
    comment_count = comment_list.count()
    return {
        "comment_list": comment_list,
        "comment_count": comment_count,
    }

@register.inclusion_tag("blog/inclusions/_comment_forms.html", takes_context=True)
def show_comment_forms(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        "form": form,
        "post": post,
    }