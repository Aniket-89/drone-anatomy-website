import os
from io import BytesIO
from PIL import Image
# import boto3
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
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


# @csrf_exempt  # Ensure CSRF exemption as per your application's security policy
# def upload_image(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         uploaded_image = request.FILES['image']

#         # Process and compress the thumbnail
#         s3_url = compress_and_upload_to_s3(uploaded_image)

#         if s3_url:
#             # Optionally, save the compressed image URL to your database or use it as needed
#             # For example, if you want to save the image URL to a Django model field:
#             # post.thumbnail_url = s3_url
#             # post.save()

#             # Return success response or redirect as per your application's logic
#             return HttpResponse(f'Image uploaded to S3. URL: {s3_url}')
#         else:
#             return HttpResponseBadRequest('Failed to upload image to S3.')

#     # Handle GET request or error cases
#     return HttpResponseBadRequest('Invalid request')

# def compress_and_upload_to_s3(image):
#     try:
#         # Open the image using Pillow
#         img = Image.open(image)

#         # Define the thumbnail size (adjust as per your requirement)
#         thumbnail_size = (300, 300)

#         # Resize the image to thumbnail size
#         img.thumbnail(thumbnail_size)

#         # Create an in-memory byte stream to save the compressed image
#         output_stream = BytesIO()

#         # Save the resized image to the byte stream with reduced quality (adjust quality as per your requirement)
#         img.save(output_stream, format='JPEG', quality=60)  # Adjust format and quality as needed

#         # Reset the stream position to the beginning
#         output_stream.seek(0)

#         # Upload the compressed image to S3
#         s3_client = boto3.client(
#             's3',
#             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#             region_name=settings.AWS_S3_REGION_NAME
#         )
#         bucket_name = settings.AWS_STORAGE_BUCKET_NAME
#         key = 'blogs/' + image.name  # Replace with your desired S3 key

#         # Upload the compressed image to S3
#         s3_client.upload_fileobj(output_stream, bucket_name, key)

#         # Return the S3 URL of the uploaded image
#         return f'https://{bucket_name}.s3.amazonaws.com/{key}'

#     except Exception as e:
#         # Handle any exceptions (e.g., image processing errors, S3 upload errors)
#         print(f"Error compressing and uploading image: {e}")
#         return None