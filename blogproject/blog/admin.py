from django.contrib import admin
from .models import Category, Tag, Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ["title", "body", "abstract", "category", "tag"]
    list_display = ["title", "created_time", "modified_time", "category", "author"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)

class CommentAdmin(admin.ModelAdmin):
    fields = ["name", "text", "email", "url", "post"]
    list_display = ["name", "email", "url", "post", "created_time"]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)

