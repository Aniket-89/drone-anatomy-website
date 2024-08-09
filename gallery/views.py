import boto3
from django.shortcuts import render
from .models import GalleryImage
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO


# Create your views here.
def gallery_view(request):
    gallery = GalleryImage.objects.all()

    context = {
        'gallery': gallery
    }
    return render(request, "gallery/gallery.html", context)


@csrf_exempt  # Ensure CSRF exemption as per your application's security policy
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']

        # Process and compress the image
        s3_url = compress_and_upload_to_s3(uploaded_image)

        if s3_url:
            # Return success response or redirect as per your application's logic
            return HttpResponse(f'Image uploaded to S3. URL: {s3_url}')
        else:
            return HttpResponseBadRequest('Failed to upload image to S3.')

    # Handle GET request or error cases
    return HttpResponseBadRequest('Invalid request')


def compress_and_upload_to_s3(image):
    try:
        # Open the image using Pillow
        img = Image.open(image)

        # Define the maximum width while maintaining the aspect ratio
        max_width = 800

        # Resize the image if it's wider than the max width
        if img.width > max_width:
            aspect_ratio = img.height / img.width
            new_height = int(max_width * aspect_ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Create an in-memory byte stream to save the compressed image
        output_stream = BytesIO()

        # Save the resized image to the byte stream with reduced quality
        img.save(output_stream, format='JPEG', quality=80)  # Adjust format and quality as needed

        # Reset the stream position to the beginning
        output_stream.seek(0)

        # Upload the compressed image to S3
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        key = 'gallery/' + image.name  # Replace with your desired S3 key

        # Upload the compressed image to S3
        s3_client.upload_fileobj(output_stream, bucket_name, key)

        # Return the S3 URL of the uploaded image
        return f'https://{bucket_name}.s3.amazonaws.com/{key}'

    except Exception as e:
        # Handle any exceptions (e.g., image processing errors, S3 upload errors)
        print(f"Error compressing and uploading image: {e}")
        return None