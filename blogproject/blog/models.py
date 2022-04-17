from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import markdown
from django.utils.html import strip_tags

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name 

class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name
class Post(models.Model):
    title = models.CharField("标题", max_length=70)
    body = models.TextField("正文")
    created_time = models.DateTimeField("创建时间", default=timezone.now())
    modified_time = models.DateTimeField("修改时间")
    abstract = models.CharField("摘要", max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
        ])

        self.abstract = strip_tags(md.convert(self.body))[:54]
        
        super().save(*args, **kwargs)

class Comment(models.Model):
    name = models.CharField("名字", max_length=30)
    text = models.TextField("内容")
    url = models.URLField("网址", blank=True)
    email = models.EmailField("邮箱")
    created_time = models.DateTimeField("创建时间", default=timezone.now())
    post = models.ForeignKey(Post, verbose_name="文章", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}_{}".format(self.name, self.text[:50])

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name