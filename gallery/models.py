import io
from PIL import Image
from django.db import models
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
        
    def save(self, *args, **kwargs):
        # Save the instance first to ensure `self.image` has a value
        super(GalleryImage, self).save(*args, **kwargs)

        if self.image:
            # Open the image using the in-memory file
            image = Image.open(self.image)
            max_width = 800

            # Resize the image if it's wider than the max width
            if image.width > max_width:
                aspect_ratio = image.height / image.width
                new_height = int(max_width * aspect_ratio)
                new_size = (max_width, new_height)

                # Resize the image
                image = image.resize(new_size, Image.Resampling.LANCZOS)

                # Save the image to a BytesIO object
                image_io = io.BytesIO()
                image.save(image_io, format=image.format, quality=80)

                # Save the new image to the ImageField
                self.image.save(self.image.name, ContentFile(image_io.getvalue()), save=False)

        # Call save again to save the resized image
        super(GalleryImage, self).save(*args, **kwargs)