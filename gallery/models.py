from django.db import models
from PIL import Image

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
        
    def save(self, *args, **kwargs):
        super(GalleryImage, self).save(*args, **kwargs)

        if self.image:
            image = Image.open(self.image.path)

            # Set the desired max width
            max_width = 800

            # Resize the image if it's wider than the max width
            if image.width > max_width:
                # Calculate the height using the same aspect ratio
                aspect_ratio = image.height / image.width
                new_height = int(max_width * aspect_ratio)
                new_size = (max_width, new_height)

                # Resize the image
                image = image.resize(new_size, Image.Resampling.LANCZOS)
                image.save(self.image.path, quality=80)