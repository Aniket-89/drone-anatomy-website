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
        # Strip HTML tags and get the first paragraph
        stripped_content = strip_tags(self.content)
        first_paragraph = stripped_content.split('\n')[1]
        # Truncate the first paragraph to 30 words
        truncated_summary = Truncator(first_paragraph).words(20, truncate=' ...')
        return truncated_summary

    class Meta:
        ordering = ['-updated_at']
