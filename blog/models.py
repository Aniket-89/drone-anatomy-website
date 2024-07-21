from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.text import Truncator
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=120, null=True, blank=True)
    content = HTMLField()
    thumbnail = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:blogdetail', kwargs={'pk': self.pk})

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return None
        
    @property
    def summary(self):
        # Assuming you want to return the first 200 characters of the content
        # and strip HTML tags for a concise summary
        return strip_tags(self.content)[:200] + ('...' if len(self.content) > 200 else '')

    class Meta:
        ordering = ['-updated_at']
