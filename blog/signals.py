import os
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import Post


@receiver(post_save, sender=Post)
def compress_image(sender, instance, **kwargs):
    if instance.thumbnail:
        img_path = instance.thumbnail.path
        image = Image.open(img_path)

        # Specify the desired dimensions (optional)
        max_width = 800
        max_height = 600
        image.thumbnail((max_width, max_height))

        # Save the image with optimized settings
        image.save(img_path, optimize=True, quality=85)