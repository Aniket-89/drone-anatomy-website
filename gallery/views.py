from django.shortcuts import render
from .models import GalleryImage


# Create your views here.
def gallery_view(request):
    gallery = GalleryImage.objects.all()

    context = {
        'gallery': gallery
    }
    return render(request, "gallery/gallery.html", context)