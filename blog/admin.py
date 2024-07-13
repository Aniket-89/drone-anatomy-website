from django.contrib import admin
from django.db import models
from .models import Post
from tinymce.widgets import TinyMCE


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author')
    list_filter = ('created_at', 'updated_at')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


