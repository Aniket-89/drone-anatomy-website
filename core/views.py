import os
from django.shortcuts import redirect, render
from django.utils import translation
from django.core.mail import send_mail, EmailMessage
from .pdf_utils import generate_pdf
from django.http import HttpResponseRedirect, JsonResponse
from .models import Subscriber
from blog.models import Post
from .forms import ContactForm, SubscriberForm, CareerForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import urllib.parse


def index_view(request):
    """
    Renders the index page with the latest 3 blog posts.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered index page.
    """
    # Get the latest 3 blog posts
    latest_blogs = Post.objects.order_by('-created_at')[:3]

    # Render the index page with the latest blog posts
    return render(request, "core/index.html", context={'latest_blogs': latest_blogs})


def agri_view(request):

    if request.method == 'POST':
        # Create a form instance with the POST data
        form = ContactForm(request.POST)

        # Validate the form data
        if form.is_valid():
            # Get the cleaned form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email to the admin
            try:
                send_mail(
                    'Test Mail',
                    f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                    settings.DEFAULT_FROM_EMAIL,  # Or use email
                    ['admin@droneanatomy.com'],
                    fail_silently=True,
                )

                # Check if the request is an AJAX request
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
                # Ensure the name here matches your URL pattern name

            # Handle exceptions while sending the email
            except Exception as e:
                error_message = f'Error: {e}'

                # Check if the request is an AJAX request
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': error_message})
                else:
                    # Render the contact page with the form and error message
                    return render(request, 'core/agri-drone.html', {'form': form, 'error': error_message})

        else:
            # Get the form errors as JSON
            errors = form.errors.as_json()

            # Check if the request is an AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Return JSON response with the form errors
                return JsonResponse({'success': False, 'errors': errors})
            else:
                # Render the contact page with the form and errors
                return render(request, 'core/agri-drone.html', {'form': form, 'errors': form.errors})

    else:
        # Create an empty form instance
        form = ContactForm()

        # Get the success query parameter from the request
        success = request.GET.get('success')

        # Render the contact page with the form and success message (if any)
        return render(request, 'core/agri-drone.html', {'form': form, 'success': success})


def about_view(request):
    """
    Renders the about page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered about page.
    """
    # Render the about page
    return render(request, "core/about.html", context={})


def career_view(request):
    """
    Renders the career page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered career page.
    """
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = CareerForm(request.POST, files=request.FILES)

        # Validate the form data
        if form.is_valid():
            # Get the cleaned form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            position = request.POST.get('position')
            message = request.POST.get('message')
            resume = form.cleaned_data.get('resume')
            
            # Generate PDF
            pdf_path = generate_pdf(name, email, message)

            # Send email to the admin
            try:
                send_career_form_email(name, email, position, message, pdf_path, resume)
        
        # Remove the temporary PDF file
                os.remove(pdf_path)

                # Check if the request is an AJAX request
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
                # Ensure the name here matches your URL pattern name

            # Handle exceptions while sending the email
            except Exception as e:
                error_message = f'Error: {e}'

                # Check if the request is an AJAX request
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': error_message})
                else:
                    # Render the contact page with the form and error message
                    return render(request, 'core/career.html', {'form': form, 'error': error_message})

        else:
            # Get the form errors as JSON
            errors = form.errors.as_json()

            # Check if the request is an AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Return JSON response with the form errors
                return JsonResponse({'success': False, 'errors': errors})
            else:
                # Render the contact page with the form and errors
                return render(request, 'core/career.html', {'form': form, 'errors': form.errors})

    else:
        # Create an empty form instance
        form = CareerForm()

        # Get the success query parameter from the request
        success = request.GET.get('success')

        # Render the contact page with the form and success message (if any)
        return render(request, 'core/career.html', {'form': form, 'success': success})

# Add comments and docstrings to the code for better readability and understanding


def contact_view(request):
    """
    Handles the contact form submission and sends an email to the admin.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered contact page or JSON response.
    """
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = ContactForm(request.POST)

        # Validate the form data
        if form.is_valid():
            # Get the cleaned form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email to the admin
            try:
                send_mail(
                    'Test Mail',
                    f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                    settings.DEFAULT_FROM_EMAIL,  # Or use email
                    ['admin@droneanatomy.com'],
                    fail_silently=True,
                )

                # Check if the request is an AJAX request
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
                # Ensure the name here matches your URL pattern name

            # Handle exceptions while sending the email
            except Exception as e:
                error_message = f'Error: {e}'

                # Check if the request is an AJAX request
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': error_message})
                else:
                    # Render the contact page with the form and error message
                    return render(request, 'core/contact.html', {'form': form, 'error': error_message})

        else:
            # Get the form errors as JSON
            errors = form.errors.as_json()

            # Check if the request is an AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Return JSON response with the form errors
                return JsonResponse({'success': False, 'errors': errors})
            else:
                # Render the contact page with the form and errors
                return render(request, 'core/contact.html', {'form': form, 'errors': form.errors})

    else:
        # Create an empty form instance
        form = ContactForm()

        # Get the success query parameter from the request
        success = request.GET.get('success')

        # Render the contact page with the form and success message (if any)
        return render(request, 'core/contact.html', {'form': form, 'success': success})
    

def whatsapp_redirect(request):
    """
    Redirects the user to a WhatsApp chat with a predefined phone number and message.

    Returns:
        HttpResponseRedirect: Redirects the user to the WhatsApp chat URL.
    """
    # Predefined phone number
    phone_number = "918130589012"
    
    # Construct the WhatsApp URL
    whatsapp_url = f"https://wa.me/{phone_number}"
    
    # Predefined message
    message = "Hello"
    
    # URL encode the message
    encoded_message = urllib.parse.quote(message)
    
    # Add the encoded message as a query parameter to the URL
    whatsapp_url += f"?text={encoded_message}"
    
    # Redirect the user to the WhatsApp chat URL
    return redirect(whatsapp_url)


@csrf_exempt
def subscribe_newsletter(request):
    """
    Subscribes a user to the newsletter by saving their email to the database.

    If the request method is POST and the form is valid, saves the email to the database
    and returns a JSON response with a success message. If the form is invalid, returns a
    JSON response with the form errors. If the request method is not POST, returns a JSON
    response with an error message.

    Args:
        request (HttpRequest): The request object.

    Returns:
        JsonResponse: A JSON response with a success message, form errors, or an error message.
    """
    # Check if request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = SubscriberForm(request.POST)

        # Check if form is valid
        if form.is_valid():
            # Get cleaned email from form
            email = form.cleaned_data['email']

            # Save email to the database
            Subscriber.objects.get_or_create(email=email)

            # Return success JSON response
            return JsonResponse({'success': True, 'message': 'Subscription successful!'})

        else:
            # Get form errors as JSON
            errors = form.errors.as_json()

            # Return JSON response with form errors
            return JsonResponse({'success': False, 'errors': errors})

    # Return JSON response with error message
    return JsonResponse({'success': False, 'message': 'Invalid request'})


def set_language(request):
    """
    Sets the user's preferred language.

    This function is called when the user changes their preferred language. It retrieves
    the user's chosen language from the request's query parameters, activates the
    corresponding language translation, and sets a cookie to remember the user's choice.
    Finally, it redirects the user back to the page they were previously viewing.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect: The response object, which redirects the user back to the page
        they were previously viewing.
    """
    # Get the user's chosen language from the request's query parameters
    user_language = request.GET.get('language', 'en')

    # Activate the corresponding language translation
    translation.activate(user_language)

    # Create a response object to redirect the user back to the page they were previously viewing
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    # Set a cookie to remember the user's language choice
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    # Return the response object
    return response


def send_career_form_email(name, email, position, message, pdf_path, resume):
    email_subject = 'Career Form'
    email_body = f'Name: {name}\nEmail: {email}\nApplying for Position: {position}\n\nMessage:\n{message}'
    recipient_list = ['admin@droneanatomy.com']
    
    email_message = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient_list,
    )
    
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            email_message.attach('CareerForm.pdf', pdf_file.read(), 'application/pdf')

    if resume:
        email_message.attach(resume.name, resume.read(), resume.content_type)

    email_message.send(fail_silently=True)