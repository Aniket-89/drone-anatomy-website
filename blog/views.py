import os
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blog/blog-list.html"

    def head(self, *args, **kwargs):
        last_post = self.get_queryset().latest("publication_date")
        response = HttpResponse(
            # RFC 1123 date format.
            headers={
                "Last-Modified": last_post.publication_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
            },
        )
        return response
    

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog-detail.html"
    context_object_name = 'obj'
    
    def head(self, pk, *args, **kwargs):
        post = self.get_object(pk=pk)
        response = HttpResponse(
            # RFC 1123 date format.
            headers={
                "Last-Modified": post.publication_date.strftime("%a, %d %b %Y %H:%M:%S GMT")
            },
        )
        return response


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        file_url = os.path.join(settings.MEDIA_URL, file.name)
        return JsonResponse({'location': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)
