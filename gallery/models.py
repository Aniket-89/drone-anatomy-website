import io
from PIL import Image
from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your models here.
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.image:
            return self.image.url
        else:
            return None
        
   